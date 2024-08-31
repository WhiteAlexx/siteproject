from django.db.models import Prefetch
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect

from myadmin.mixins import AdminMixin
from myadmin.utils import q_search
from common.mixins import CacheMixin, get_context_categories
from goods.models import Categories
from orders.models import Order, OrderItem
from users.models import User

# Create your views here.

class MyAdminView(LoginRequiredMixin, TemplateView):
    template_name = 'myadmin/myadmin.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_superuser:
            status = self.kwargs.get('order_status')

            query = self.request.GET.get("q")

            if status == 'process':
                status = 'В обработке'
            elif status == 'done':
                status = 'Собран'
            elif status == 'delivery':
                status = 'В пути'

            if query:
                orders = q_search(query)
            elif status == "all":
                orders = Order.objects.all().prefetch_related(
                    Prefetch(
                        "orderitem_set",
                        queryset=OrderItem.objects.select_related("product")
                    )
                ).order_by("id")
            else:
                orders = get_orders(status)
        context = super().get_context_data(**kwargs)
        context['orders'] = orders
        context['title'] = 'Заказы'

        return context


@login_required
def orderdone(request):
    user = request.user
    if user.is_superuser:

        order_id = request.POST.get("order_id")
        status = request.POST.get("status")
        order = Order.objects.get(id=order_id)
        # order = self.get_order(order_id=order_id)     #   => mixin

        if status == 'В обработке':
            order.status = 'Собран'
        elif status == 'Собран':
            order.status = 'В пути'
        order.save()

        orders = get_orders(status)

        order_items_html = render_to_string(
                "myadmin/includes/included_myadmin.html", {"orders": orders}, request=request)

        response_data = {
            "order_items_html": order_items_html,
        }
        return JsonResponse(response_data)

    else:
        return redirect('user:login')

def get_orders(status):
    return Order.objects.filter(status=status).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product")
                )
            ).order_by("id")


class MyAdminGoods(LoginRequiredMixin, TemplateView):
    template_name = 'myadmin/goods.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_context_categories()
        context['title'] = 'Товары'

        return context
