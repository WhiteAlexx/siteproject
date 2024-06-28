from django.template.loader import render_to_string
from django.urls import reverse
from carts.models import Cart
from carts.utils import get_endng, get_user, get_user_carts


class CartMixin:

    def get_cart(self, request, product=None, cart_id=None):
        if request.user.is_authenticated:
            query_kwargs = {'user': request.user}
        else:
            query_kwargs = {'session_key': request.session.session_key}

        if product:
            query_kwargs['product'] = product
        if cart_id:
            query_kwargs['id'] = cart_id
        return Cart.objects.filter(**query_kwargs).first()

    def render_cart(self, request):
        user_cart = get_user_carts(request)
        context = {'carts': user_cart}

        #If referer page is create_order add key orders: True to context
        referer = request.META.get('HTTP_REFERER')
        if reverse('orders:create_order') in referer:
            context['order'] = True

        tovar = get_endng(request)

        if request.user.is_authenticated:
            user_user = get_user(request)
            return render_to_string(
                'carts/includes/included_cart.html', {'carts': user_cart, "tovar": tovar, "form": user_user}, request=request)
        else:
            return render_to_string(
                'carts/includes/included_cart.html', {'carts': user_cart, "tovar": tovar}, request=request)
