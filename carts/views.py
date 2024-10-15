from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View

from carts.mixins import CartMixin
from carts.models import Cart
from carts.utils import get_select_quantity, get_total_price, get_user, get_user_carts, get_endng
from goods.models import Products


class CartAddView(CartMixin, View):

    def post(self, request):

        product_id = request.POST.get("product_id")
        count_res = request.POST.get("count_res")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            if product.is_residual:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=count_res)
            else:
                cart.quantity += product.count_for
            cart. save()
        else:
            if product.is_residual:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=count_res)
            else:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=product.count_for)

        response_data = {
            "message": "Товар добавлен в корзину",
            'cart_items_html': self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartAddMidView(CartMixin, View):

    def post(self, request):

        product_id = request.POST.get("product_id")
        count_res = request.POST.get("count_res")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            if product.is_residual:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=count_res)
            else:
                cart.quantity += product.count_for_mid
            cart. save()
        else:
            if product.is_residual:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=count_res)
            else:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=product.count_for_mid)

        response_data = {
            "message": "Товар добавлен в корзину",
            'cart_items_html': self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartAddLowView(CartMixin, View):

    def post(self, request):

        product_id = request.POST.get("product_id")
        count_res = request.POST.get("count_res")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            if product.is_residual:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=count_res)
            else:
                cart.quantity += int(product.count_for_low)
            cart. save()
        else:
            if product.is_residual:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=count_res)
            else:
                Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product, quantity=product.count_for_low)

        response_data = {
            "message": "Товар добавлен в корзину",
            'cart_items_html': self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):

    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_cart(request, cart_id=cart_id)

        cart.quantity = request.POST.get('quantity')
        cart.save()

        quantity = int(cart.quantity)

        response_data = {
            "message": "Количество изменено",
            'quantity': quantity,
            'cart_items_html': self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):

    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_cart(request, cart_id=cart_id)

        quantity = int(cart.quantity)
        cart. delete()

        user_cart = get_user_carts(request)
        context = {'carts': user_cart}
        clss = 1
        if not context.get('carts'):
            clss = 0

        response_data = {
            "message": "Товар удален из корзины",
            'quantity': quantity,
            'clss': clss,
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
    select_quantity = get_select_quantity(request)
    total_price = get_total_price(request)


    if request.user.is_authenticated:
        user_user = get_user(request)
        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", {
                "carts": user_cart, "select_quantity": select_quantity, "total_price": total_price, 
                "tovar": tovar, "form": user_user}, request=request)
    else:
        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", {
                "carts": user_cart, "select_quantity": select_quantity, "total_price": total_price, 
                "tovar": tovar}, request=request)

    response_data = {
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)
