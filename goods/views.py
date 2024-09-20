import time
from typing import Any
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from carts.models import Cart
from carts.utils import get_user_carts, get_endng, get_select_quantity, get_total_price
from common.mixins import get_context_categories
from goods.models import Categories, Products
from goods.utils import q_search
from favorites.utils import get_favorite


class CatalogView(ListView):

    model = Products
    # queryset = Products.objects.all().order_by('-id')
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 8
    # allow_empty = False     #Автоматически генерирует 'error404', если в категории нет товаров

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')

        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
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
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары в наличии'
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['slug_url'] = self.kwargs.get('category_slug')
        context['categories'] = get_context_categories()
        context['favorites'] = get_favorite(self.request)
        return context

    def auto_update_is_neo(self):
        category_slug = self.kwargs.get('category_slug')

        if category_slug == 'is_neo':
            # сюда поставить проверку на месяц 2592000сек
            query_create_date = super().get_queryset().filter(is_neo=True)
            for product in query_create_date:

                if time.time() - time.mktime(time.strptime(product.created_time_stamp.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")) > 2592000:
                    product.is_neo = False
                    product.save()

        return None

# scheduler = sched.scheduler()
# event_time = datetime.datetime.now().replace(hour=10, minute=15, second=0, microsecond=0)
# scheduler.enterabs(event_time.timestamp(), 1, CatalogView.auto_update_is_neo, ())
# scheduler.run()


class ProductView(DetailView):

    # model = Products
    # slug_field = 'slug'
    template_name = 'goods/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['categories'] = get_context_categories()
        context['favorites'] = get_favorite(self.request)
        carts = Cart.objects.filter(product=self.object.id)
        context['list_quantity'] = [str(int(cart.quantity)) for cart in carts]
        return context

# def catalog(request, category_slug=None):

#     page = request.GET.get("page", 1)
#     on_sale = request.GET.get("on_sale", None)
#     order_by = request.GET.get("order_by", None)
#     query = request.GET.get("q", None)

#     if category_slug == "tovary":
#         goods = Products.objects.exclude(category__slug__icontains='v-puti').exclude(category__slug__icontains='udalennye')
#     elif query:
#         goods = q_search(query)
#     else:
#         goods = Products.objects.filter(category__slug=category_slug)

#     if on_sale:
#         goods = goods.filter(discount__gt=0)

#     if order_by and order_by != "default":
#         goods = goods.order_by(order_by)

#     paginator = Paginator(goods, 6)
#     crrnt_pg = paginator.page(page)

#     print(crrnt_pg.object_list)

#     context = {
#         "title": "Товары в наличии",
#         "goods": crrnt_pg,
#         "slug_url": category_slug,
#     }
#     return render(request, "goods/catalog.html", context)

# def product(request, product_id=False, product_slug=False):

#     if product_id:
#         product = Products.objects.get(id=product_id)
#     else:
#         product = Products.objects.get(slug=product_slug)

#     context = {"product": product}
#     return render(request, "goods/product.html", context=context)
