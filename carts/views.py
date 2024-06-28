from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views import View
from num2words import num2words

from carts.mixins import CartMixin
from carts.models import Cart
from carts.utils import get_user, get_user_carts, get_endng
from goods.models import Products
from orders.forms import CreateOrderForm


class CartAddView(CartMixin, View):

    def post(self, request):

        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart. save()
        else:
            Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                session_key=request.session.session_key if not request.user.is_authenticated else None,
                                product=product, quantity=1)

        response_data = {
            'cart_items_html': self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):

    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_cart(request, cart_id=cart_id)

        cart.quantity = request.POST.get('quantity')
        cart.save()

        quantity = cart.quantity

        response_data = {
            'quantity': quantity,
            'cart_items_html': self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):

    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_cart(request, cart_id=cart_id)

        quantity = cart.quantity
        cart. delete()

        response_data = {
            'quantity': quantity,
            'cart_items_html': self.render_cart(request),
        }

        return JsonResponse(response_data)


def cart_select(request):

    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)

    if cart.select_buy is True:
        cart.select_buy = False
    else:
        cart.select_buy = True
    cart.save()

    user_cart = get_user_carts(request)
    tovar = get_endng(request)

    if request.user.is_authenticated:
        user_user = get_user(request)
        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar, "form": user_user}, request=request)
    else:
        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar}, request=request)

    response_data = {
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)



# def cart_add(request):

#     product_id = request.POST.get("product_id")
#     product = Products.objects.get(id=product_id)

#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, product=product)

#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(user=request.user, product=product, quantity=1)

#     else:
#         carts = Cart.objects.filter(
#             session_key=request.session.session_key, product=product)

#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(
#                 session_key=request.session.session_key, product=product, quantity=1
#             )

#     user_cart = get_user_carts(request)
#     tovar = get_endng(request)

#     if request.user.is_authenticated:
#         user_user = get_user(request)
#         cart_items_html = render_to_string(
#             "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar, "form": user_user}, request=request)
#     else:
#         cart_items_html = render_to_string(
#             "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar}, request=request)

#     response_data = {
#         "cart_items_html": cart_items_html,
#     }

#     return JsonResponse(response_data)


# def cart_change(request):

#     cart_id = request.POST.get("cart_id")
#     quantity = request.POST.get("quantity")

#     cart = Cart.objects.get(id=cart_id)

#     cart.quantity = quantity
#     cart.save()

#     user_cart = get_user_carts(request)
#     tovar = get_endng(request)

#     if request.user.is_authenticated:
#         user_user = get_user(request)
#         cart_items_html = render_to_string(
#             "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar, "form": user_user}, request=request)
#     else:
#         cart_items_html = render_to_string(
#             "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar}, request=request)

#     response_data = {
#         "cart_items_html": cart_items_html,
#     }

#     return JsonResponse(response_data)


# def cart_remove(request):

#     cart_id = request.POST.get("cart_id")

#     cart = Cart.objects.get(id=cart_id)
#     quantity = cart.quantity
#     cart.delete()

#     user_cart = get_user_carts(request)
#     tovar = get_endng(request)

#     if request.user.is_authenticated:
#         user_user = get_user(request)
#         cart_items_html = render_to_string(
#             "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar, "form": user_user}, request=request)
#     else:
#         cart_items_html = render_to_string(
#             "carts/includes/included_cart.html", {"carts": user_cart, "tovar": tovar}, request=request)

#     response_data = {
#         "cart_items_html": cart_items_html,
#     }

#     return JsonResponse(response_data)
