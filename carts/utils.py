from carts.models import Cart
from orders.forms import CreateOrderForm


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)#.select_related('product')

    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)#.select_related('product')

def get_user(request):
    # if request.user.is_authenticated:
    initial = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'telnmbr': request.user.telnmbr,
        'adres': request.user.adres,
    }
    return CreateOrderForm(initial=initial)
