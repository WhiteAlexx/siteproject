import imp
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories, Products

# Create your views here.
def index(request):
      
    categories = Categories.objects.exclude(slug__contains='tovary')  #Фильтр без все и в пути
    #product = Products.objects.exclude(category__name__icontains='в пути')

    context: dict[str, str] = {
        'title': 'Домашняя',
        'categories': categories,
        #'product': product
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': '42',
        'cntnt': '42',
        'text_on_page': 'The Ultimate Question of Life, the Universe, and Everything',
    }

    return render(request, 'main/delivery.html', context)

def delivery(request):
    context: dict[str, str] = {
        'title': 'О доставке',
        'cntnt': 'Доставка',
        'text_on_page': 'Рассказать об условиях доставки',
    }

    return render(request, 'main/delivery.html', context)


def payment(request):
    return render(request, 'main/payment.html')
