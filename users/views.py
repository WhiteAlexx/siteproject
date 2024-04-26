from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from carts.models import Cart
from carts.utils import get_user_carts, get_endng
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if session_key:
                    carts_sess = Cart.objects.filter(session_key=session_key)
                    carts_user = Cart.objects.filter(user=request.user)

                    for cart_user in carts_user:
                        for cart_sess in carts_sess:
                            if cart_user.product.name == cart_sess.product.name:
                                cart_user.quantity += cart_sess.quantity
                                cart_user.select_buy = True
                                cart_user.save()
                                cart_sess.delete()
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        "title": "Авторизация",
        'form': form
        }
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f"{user.username}, Вы успешно зарегистрировались и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Регистрация",
        'form': form
    }
    return render(request, "users/registration.html", context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль обновлён")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product")
                )
            )
            .order_by("-id")
        )

    tovar = get_endng(request)

    context = {
        "title": "Кабинет",
        "form": form,
        "orders": orders,
        "tovar": tovar,
        }
    return render(request, "users/profile.html", context)

def users_cart(request):

    tovar = get_endng(request)

    return render(request, 'users/users_cart.html', {"tovar": tovar, "title": "Корзина товаров"})

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

@login_required
def payment(request):

    order_id = request.POST.get("order_id")
    amount_order = Order.objects.get(id=order_id)
    # order = amount_order.id
    amount = amount_order.total_cost
    payment_html = render_to_string(
            "users/includes/included_payment.html", {"order": order_id, "amount": amount}, request=request)

    response_data = {
        "payment_html": payment_html,
    }
    return JsonResponse(response_data)
