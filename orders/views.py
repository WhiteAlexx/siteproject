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

# def cart_change(request):
#     cart_id = request.POST.get("cart_id")
#     quantity = request.POST.get("quantity")

#     cart = Cart.objects.get(id=cart_id)

#     cart.quantity = quantity
#     cart.save()
#     update_quantity = cart.quantity

#     cart = get_user_carts(request)
#     cart_items_html = render_to_string(
#         "orders/create_order.html", {"carts": cart}, request=request)

#     response_data = {
#         "message": "Количество изменено",
#         "cart_items_html": cart_items_html,
#         "quantity": update_quantity,
#     }

#     return JsonResponse(response_data)

# def cart_remove(request):

#     cart_id = request.POST.get("cart_id")

#     cart = Cart.objects.get(id=cart_id)
#     quantity = cart.quantity
#     cart.delete()

#     user_cart = get_user_carts(request)
#     cart_items_html = render_to_string(
#         "orders/create_order.html", {"carts": user_cart}, request=request)

#     response_data = {
#         "message": "Товар удалён",
#         "cart_items_html": cart_items_html,
#         "quantity_deleted": quantity,
#     }

#     return JsonResponse(response_data)
