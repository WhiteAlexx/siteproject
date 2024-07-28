from num2words import num2words
from carts.models import Cart
from orders.forms import CreateOrderForm


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).order_by('-id')

    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).order_by('-id')

def get_user(request):
    if request.user.is_authenticated:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'telnmbr': request.user.telnmbr,
            'adres': request.user.adres,
        }
    return CreateOrderForm(initial=initial)

def get_endng(request):
    user_cart = get_user_carts(request)
    num = user_cart.select_quantity()
    endng = list(num2words(num, lang='ru'))[-1]

    if endng == 'н':
        return 'товар на сумму'
    elif endng in ['ь', 'к', 'т', 'о']:
        return 'товаров на сумму'
    else:
        return 'товара на сумму'
