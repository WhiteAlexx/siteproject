from typing import Any
from django.views.generic import TemplateView

from common.mixins import get_context_categories
from carts.utils import get_endng, get_select_quantity, get_total_price


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Домашняя'
        context['select_quantity'] = get_select_quantity(self.request)
        context['total_price'] = get_total_price(self.request)
        context['tovar'] = get_endng(self.request)
        context['categories'] = get_context_categories()
        context['user_name'] = self.request.user.username
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = '42'
        context['cntnt'] = '42'
        context['text_on_page'] = 'The Ultimate Question of Life, the Universe, and Everything'
        return context


class DeliveryView(TemplateView):
    template_name ='main/delivery.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О доставке'
        context['cntnt'] = 'Доставка'
        context['text_on_page'] = 'Рассказать об условиях доставки'
        return context
