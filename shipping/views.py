from django.views.generic import DetailView, ListView

from common.mixins import get_context_categories, get_context_user
from goods.models import Products
from carts.utils import get_endng, get_select_quantity, get_total_price
from favorites.utils import get_favorite


class ShippingView(ListView):

    template_name = 'shipping/shipping.html'
    context_object_name = 'shipp'
    paginate_by = 20

    def get_queryset(self):
        shipp = Products.objects.filter(category__name__icontains='в пути')
        return shipp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заказать в пути'
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['categories'] = get_context_categories()
        context['user_name'] = get_context_user(self.request)
        favorites = get_favorite(self.request)
        context['favorites'] = list(favorite.product.id for favorite in favorites)
        return context


class ProductView(DetailView):

    template_name = 'shipping/product.html'
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
        return context
