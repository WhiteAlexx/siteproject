from django.db.models import Prefetch
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

from common.mixins import CacheMixin
from goods.models import Categories
from orders.models import Order, OrderItem
from users.models import User

# Create your views here.

class MyAdminView(LoginRequiredMixin, TemplateView, CacheMixin):
    template_name = 'myadmin/myadmin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заказы'
        context['categories'] = Categories.objects.exclude(slug__contains='tovary')
        context['users'] = User.objects.all()

    #   ВЫБИРАЕТ ВСЕ ЗАКАЗЫ. ВОЗМОЖНО, НУЖНО СДЕЛАТЬ ФИЛЬТР ПО СТАТУСУ
        # status = 'В обработке'
        orders = Order.objects.all().prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product")
                )
            ).order_by("id")

        context['orders'] = orders
        # context['orders'] = self.set_get_cache(orders, f'user_{self.request.user.id}_orders', 60 * 2)
        return context


@login_required
def orderdone(request):

    order_id = request.POST.get("order_id")
    bttnname = request.POST.get("bttnName")
    order = Order.objects.get(id=order_id)

    if 'Собрать' in bttnname:
        order.status = 'Собран'
        status = 'В обработке'
    elif 'Отправить' in bttnname:
        order.status = 'В пути'
        status = 'Собран'
    order.save()

    orders = get_orders(status)

    order_items_html = render_to_string(
            "myadmin/includes/included_myadmin.html", {"orders": orders}, request=request)

    response_data = {
        "order_items_html": order_items_html,
    }
    return JsonResponse(response_data)

def get_orders(status):
    return Order.objects.filter(status=status).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product")
                )
            ).order_by("id")
    # return orders