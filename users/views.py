from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.db.models import Prefetch
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from carts.models import Cart
from carts.utils import get_user_carts, get_endng
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from users.models import User

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


# def pass_reset_form(request):
#     form = UserPassResetForm
#     return render(request, "users/password_reset_form.html", {"form": form, "title": "Сброс пароля"})


# def pass_reset_done(request):
#     if request.method == 'POST':
#         form = UserPassResetForm(data=request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             users = User.objects.all()
#             for user in users:
#                 if email == user.email:
#                     site_name = 'Оптовые закупки из Китая'
#                     protocol = 'https'
#                     domain = request.get_host()
#                     url = 'users/password_reset_confirm'
#                     # uid = ''
#                     token = default_token_generator
#                     subject = f'Сброс пароля на сайте { site_name }'
#                     message = f"Вы получили это письмо, поскольку запросили сброс пароля для своей учетной записи на сайте { site_name }.\n\
#     Пожалуйста, перейдите на следующую страницу и выберите новый пароль:\n\
#     { protocol }://{ domain }{ url }/{ token }/\n\
#     Ваше имя пользователя, если вы забыли:{ user.get_username }\n\
#     Спасибо за использование нашего сайта!\n\
#     Команда { site_name }"
#                     from_email = 'webmaster@localhost'
#                     recipient_list = [email,]
#                     send_mail(subject, message, from_email, recipient_list,)

#     return render(request, "users/password_reset_done.html", {"title": "Сброс пароля"})


# def pass_reset_confirm(request):
#     form = UserPassSetForm
#     return render(request, "users/password_reset_confirm.html", {"form": form, "title": "Сброс пароля"})


# def pass_reset_complete(request):
#     if request.method == 'POST':
#         form = UserPassSetForm(data=request.POST)
#         if form.is_valid():
#             print(request.POST)
#     return render(request, "users/password_reset_complete.html", {"title": "Сброс пароля"})
