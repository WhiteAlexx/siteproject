from typing import Any
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from common.mixins import get_context_categories
from goods.models import Categories, Products
from carts.utils import get_user_carts, get_endng, get_select_quantity, get_total_price


class ShippingView(ListView):

    template_name = 'shipping/shipping.html'
    context_object_name = 'shipp'
    paginate_by = 6

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
        # context['slug_url'] = 'get_queryset.category_slug'
        return context

# def shipping(request):

#     page = request.GET.get("page", 1)
#     shipp = Products.objects.filter(category__name__icontains='в пути')

#     paginator = Paginator(shipp, 6)
#     crrnt_pg = paginator.page(page)

#     context = {
#         "title": "Заказать в пути",
#         "shipp": crrnt_pg,
#     }
#     return render(request, "shipping/shipping.html", context)


class ProductView(DetailView):

    # model = Products
    # slug_field = 'slug'
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
        return context

# def product(request, product_id=False, product_slug=False):

#     if product_id:
#         product = Products.objects.get(id=product_id)
#     else:
#         product = Products.objects.get(slug=product_slug)

#     context = {
#        'product': product
#     }
#     return render(request, "shipping/product.html", context=context)
