from typing import Any
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from common.mixins import get_context_categories
from goods.models import Categories, Products
from carts.utils import get_user_carts, get_endng, get_select_quantity, get_total_price
from orders.models import Order


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Домашняя'
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['categories'] = get_context_categories()
        return context

# def index(request):

#     categories = get_context_categories()  #Фильтр без все и в пути
#     #product = Products.objects.exclude(category__name__icontains='в пути')

#     context: dict[str, str] = {
#         'title': 'Домашняя',
#         'categories': categories,
#         #'product': product
#     }

#     return render(request, 'main/index.html', context)


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = '42'
        context['cntnt'] = '42'
        context['text_on_page'] = 'The Ultimate Question of Life, the Universe, and Everything'
        return context

# def about(request):
#     context: dict[str, str] = {
#         'title': '42',
#         'cntnt': '42',
#         'text_on_page': 'The Ultimate Question of Life, the Universe, and Everything',
#     }

#     return render(request, 'main/delivery.html', context)


class DeliveryView(TemplateView):
    template_name ='main/delivery.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О доставке'
        context['cntnt'] = 'Доставка'
        context['text_on_page'] = 'Рассказать об условиях доставки'
        return context

# def delivery(request):
#     context: dict[str, str] = {
#         'title': 'О доставке',
#         'cntnt': 'Доставка',
#         'text_on_page': 'Рассказать об условиях доставки',
#     }

#     return render(request, 'main/delivery.html', context)
