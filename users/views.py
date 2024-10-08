from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Prefetch
from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from carts.models import Cart
from carts.utils import get_endng, get_select_quantity, get_total_price
from common.mixins import CacheMixin, get_context_categories, get_context_user
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

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
        context['categories'] = get_context_categories()
        context['user_name'] = get_context_user(self.request)
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
        context['categories'] = get_context_categories()
        context['user_name'] = get_context_user(self.request)
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
        context['categories'] = get_context_categories()
        context['user_name'] = get_context_user(self.request)

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
        context['categories'] = get_context_categories()
        context['user_name'] = get_context_user(self.request)
        return context


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

@login_required
def payment(request):

    order_id = request.POST.get("order_id")
    amount_order = Order.objects.get(id=order_id)
    amount = amount_order.total_cost
    payment_html = render_to_string(
            "users/includes/included_payment.html", {"order": order_id, "amount": amount}, request=request)

    response_data = {
        "payment_html": payment_html,
    }
    return JsonResponse(response_data)
