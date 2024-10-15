from datetime import timedelta, datetime
from django.db.models.base import Model as Model
from django.views.generic import DetailView, ListView

from carts.models import Cart
from carts.utils import get_endng, get_select_quantity, get_total_price
from common.mixins import get_context_categories, get_context_user
from goods.models import Products
from goods.utils import q_search
from favorites.utils import get_favorite


class CatalogView(ListView):

    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 20
    # allow_empty = False     #Автоматически генерирует 'error404', если в категории нет товаров

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')

        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if category_slug == "tovary":
            goods = super().get_queryset().exclude(category__slug__icontains='v-puti').exclude(category__slug__icontains='udalennye')
        elif category_slug == 'is_neo':
            super().get_queryset().filter(created_time_stamp__lte=datetime.now() - timedelta(30)).update(is_neo=False)
            goods = super().get_queryset().filter(is_neo=True)
        elif category_slug == 'favorites':
            favorites = get_favorite(self.request)
            goods = super().get_queryset().filter(id__in=list(favorite.product.id for favorite in favorites))
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
        context['user_name'] = get_context_user(self.request)
        favorites = get_favorite(self.request)
        context['favorites'] = list(favorite.product.id for favorite in favorites)
        return context


class ProductView(DetailView):

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
        context['user_name'] = get_context_user(self.request)
        favorites = get_favorite(self.request)
        context['favorites'] = list(favorite.product.id for favorite in favorites)
        carts = Cart.objects.filter(product=self.object.id)
        context['list_quantity'] = [str(int(cart.quantity)) for cart in carts]
        return context
