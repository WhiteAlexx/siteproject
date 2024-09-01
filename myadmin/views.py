import time
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
from goods.models import Categories, Products
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


class MyAdminGoods(LoginRequiredMixin, ListView):

    model = Products
    # queryset = Products.objects.all().order_by('-id')
    template_name = 'myadmin/goods.html'
    context_object_name = 'goods'
    paginate_by = 20

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')

        query = self.request.GET.get("q")

        if category_slug == "tovary":
            goods = super().get_queryset().exclude(category__slug__icontains='v-puti').exclude(category__slug__icontains='udalennye')
        elif category_slug == 'is_neo':
            # сюда поставить проверку на месяц 2592000сек
            query_create_date = super().get_queryset().filter(is_neo=True)
            for product in query_create_date:

                if time.time() - time.mktime(time.strptime(product.created_time_stamp.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")) > 2592000:
                    product.is_neo = False
                    product.save()
            goods = super().get_queryset().filter(is_neo=True)
        elif category_slug == 'v-puti':
            goods = super().get_queryset().filter(category__slug__icontains='v-puti')
        elif category_slug == 'all':
            goods = super().get_queryset().all()
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)

        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары'
        context['slug_url'] = self.kwargs.get('category_slug')
        context['categories'] = get_context_categories()

        return context

