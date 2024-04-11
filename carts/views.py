from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user, get_user_carts
from goods.models import Products
from orders.forms import CreateOrderForm


# Create your views here.


def cart_add(request):

    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product
        )

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1
            )

    user_cart = get_user_carts(request)
    user_user = get_user(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart, "form": user_user}, request=request)

    response_data = {
        # "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_change(request):

    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    update_quantity = cart.quantity

    user_cart = get_user_carts(request)
    user_user = get_user(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart, "form": user_user}, request=request)

    response_data = {
        # "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": update_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):

    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    user_user = get_user(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart, "form": user_user}, request=request)

    response_data = {
        # "message": "Товар удалён",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)

def cart_select(request, cart_id):

    # cart_id = request.POST.get("cart_id")
    # product = Products.objects.get(slug=product_slug)
    # selection = request.POST.get("selection")

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, cart_id=cart_id)

        cart = carts.first()
        if cart.select_buy is True:
            cart.select_buy = False
        else:
            cart.select_buy = True

        cart.save()

    return redirect(request.META['HTTP_REFERER'])

    # cart = Cart.objects.get(id=cart_id)

    # cart.select_buy = selection
    # cart.save()

    # user_cart = get_user_carts(request)
    # user_user = get_user(request)
    # cart_items_html = render_to_string(
    #     "carts/includes/included_cart.html", {"carts": user_cart, "form": user_user}, request=request)

    # response_data = {
    #     # "message": "Количество изменено",
    #     "cart_items_html": cart_items_html,
    # }

    # return JsonResponse(response_data)
