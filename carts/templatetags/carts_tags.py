from django import template

from carts.models import Cart
from carts.utils import get_endng, get_user, get_user_carts

register = template.Library()

@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)

@register.simple_tag()
def user_user(request):
    return get_user(request)

@register.simple_tag()
def tovar_endng(request):
    return get_endng(request)
