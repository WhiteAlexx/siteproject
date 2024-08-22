from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Prefetch, QuerySet
from django.db.models.base import Model as Model
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from carts.models import Cart
from carts.utils import get_user_carts, get_endng, get_select_quantity, get_total_price
from common.mixins import CacheMixin
from goods.models import Categories
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from users.models import User

class UserLoginView(LoginView):

    template_name = 'users/login.html'
    form_class = UserLoginForm
    # success_url = reverse_lazy('main:index')

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse_lazy('user:logout'):
            return redirect_page
        return reverse_lazy('main:index')

    def form_valid(self, form):
        session_key = self.request.session.session_key

        user = form.get_user()

        if user:
            auth.login(self.request, user)
            messages.success(self.request, f"{user.username}, Вы вошли в аккаунт")

            if session_key:
                old_carts = Cart.objects.filter(user=user)
                if old_carts.exists():
                    old_carts.delete()
                Cart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['categories'] = Categories.objects.exclude(slug__contains='tovary')
        return context


class UserRegistrationView(CreateView):

    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(self.request, f"{user.username}, Вы успешно зарегистрировались и вошли в аккаунт")
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['categories'] = Categories.objects.exclude(slug__contains='tovary')
        return context


class UserProfileView(LoginRequiredMixin, CacheMixin, UpdateView):

    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Профиль обновлён")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Произошла ошибка')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Кабинет'
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['categories'] = Categories.objects.exclude(slug__contains='tovary')

        # orders = cache.get(f'orders_for_user_{self.request.user.id}')
        # if not orders:
        orders = Order.objects.filter(user=self.request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product")
                )
            ).order_by("-id")
            # cache.set(f'orders_for_user_{self.request.user.id}', orders, 60)

        context['orders'] = self.set_get_cache(orders, f'user_{self.request.user.id}_orders', 60 * 2)
        return context


class UserCartView(TemplateView):

    template_name = 'users/users_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина товаров'
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['categories'] = Categories.objects.exclude(slug__contains='tovary')
        return context


# def users_cart(request):

#     tovar = get_endng(request)

#     return render(request, 'users/users_cart.html', {"tovar": tovar, "title": "Корзина товаров"})


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



# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)

#             session_key = request.session.session_key

#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f"{username}, Вы вошли в аккаунт")

#                 if session_key:
#                     carts_sess = Cart.objects.filter(session_key=session_key)
#                     carts_user = Cart.objects.filter(user=request.user)

#                     for cart_user in carts_user:
#                         for cart_sess in carts_sess:
#                             if cart_user.product.name == cart_sess.product.name:
#                                 cart_user.quantity += cart_sess.quantity
#                                 cart_user.select_buy = True
#                                 cart_user.save()
#                                 cart_sess.delete()
#                     Cart.objects.filter(session_key=session_key).update(user=user)

#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('user:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))

#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserLoginForm()

#     context = {
#         "title": "Авторизация",
#         'form': form
#         }
#     return render(request, "users/login.html", context)


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()

#             session_key = request.session.session_key

#             user = form.instance
#             auth.login(request, user)

#             if session_key:
#                 Cart.objects.filter(session_key=session_key).update(user=user)

#             messages.success(request, f"{user.username}, Вы успешно зарегистрировались и вошли в аккаунт")
#             return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserRegistrationForm()

#     context = {
#         "title": "Регистрация",
#         'form': form
#     }
#     return render(request, "users/registration.html", context)


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Профиль обновлён")
#             return HttpResponseRedirect(reverse('user:profile'))
#     else:
#         form = ProfileForm(instance=request.user)

#     orders = (
#         Order.objects.filter(user=request.user)
#             .prefetch_related(
#                 Prefetch(
#                     "orderitem_set",
#                     queryset=OrderItem.objects.select_related("product")
#                 )
#             )
#             .order_by("-id")
#         )

#     tovar = get_endng(request)

#     context = {
#         "title": "Кабинет",
#         "form": form,
#         "orders": orders,
#         "tovar": tovar,
#         }
#     return render(request, "users/profile.html", context)
