from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from carts.models import Cart
from carts.utils import get_endng, get_select_quantity, get_total_price
from common.mixins import get_context_categories, get_context_user
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


class CreateOrderView(LoginRequiredMixin, FormView):

    template_name = 'orders/create_order.html'
    form_class = CreateOrderForm
    success_url = reverse_lazy('users:profile')

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['telnmbr'] = self.request.user.telnmbr
        initial['adres'] = self.request.user.adres

        return initial

    def form_valid(self, form):

        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():

                    total_cost = 0
                    for cart_item in cart_items:
                        if cart_item.select_buy is True:
                            quantity = cart_item.quantity
                            price = get_price(user, cart_item, quantity)
                            total_cost += price * quantity


                    # Создать заказ
                    order = Order.objects.create(
                        user=user,
                        telnmbr=form.cleaned_data['telnmbr'],
                        adres=form.cleaned_data['adres'],
                        total_cost=total_cost
                    )
                    # Создать заказанные товары
                    total_cost = 0
                    cntr = 0

                    for cart_item in cart_items:
                        if cart_item.select_buy is True:
                            product = cart_item.product
                            name = cart_item.product.name
                            quantity = cart_item.quantity
                            price = get_price(user, cart_item, quantity)
                            unit = product.unit


                            cost = price * quantity
                            total_cost += cost

                            if product.quantity < quantity and product.category.name != 'Товары в пути' and product.is_residual is False:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе.\
                                                    В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                                unit=unit,
                            )
                            if not product.is_residual:
                                product.quantity -= quantity
                                product.save()
                            if product.is_residual:
                                if cntr == 0:
                                    res_list = product.residual_list_float()
                                else:
                                    res_list = [float(res) for res in residuals.split()]
                                res_list.remove(float(quantity))
                                res_list = [str(quant) for quant in res_list]
                                residuals = ' '.join(res_list)
                                product.residual = residuals
                                if residuals == '':
                                    product.is_residual = False
                                product.save()
                                cntr += 1

                            # Очистить корзину пользователя после создания заказа
                            cart_item.delete()

                    messages.success(self.request, 'Заказ оформлен!')
                    return redirect('user:profile')
        except ValidationError as e:
            messages.success(self.request, str(e))
            return redirect('orders:create_order')

    def form_invalid(self, form):
        messages.error(self.request, 'Заполните все обязательные поля')
        return redirect('orders:create_order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['categories'] = get_context_categories()
        context['user_name'] = get_context_user(self.request)
        return context

def get_price(user, cart_item, quantity):
    if cart_item.product.is_residual:
        if user.groups.name == 'Опт':
            price = cart_item.product.sell_price_low()
        elif quantity < cart_item.product.count_for_mid:
            price = cart_item.product.sell_price()
    else:
        if user.groups.name == 'Опт':
            price = cart_item.product.sell_price_low()
        elif quantity >= cart_item.product.count_for_mid:
            price = cart_item.product.sell_price_mid()
        elif quantity < cart_item.product.count_for_mid:
            price = cart_item.product.sell_price()

    return price
