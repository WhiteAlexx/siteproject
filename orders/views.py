from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart, CartQueryset
from carts.utils import get_user_carts
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem, OrderitemQueryset

# Create your views here.
@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():

                        total_cost = 0
                        for cart_item in cart_items:
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity
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
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.name
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity
                            unit = cart_item.unit

                            cost = price * quantity
                            total_cost += cost

                            if product.quantity < quantity and product.category.name != 'Товары в пути':
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                                unit=unit,
                            )

                            product.quantity -= quantity
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'telnmbr': request.user.telnmbr,
            'adres': request.user.adres,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Оформление заказа',
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context=context)
