from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products

# Create your views here.
def shipping(request, page=1):

    shipp = Products.objects.filter(category__name__icontains='в пути')

    paginator = Paginator(shipp, 3)
    crrnt_pg = paginator.page(page)

    context = {
        "title": "Заказать в пути",
        "shipp": crrnt_pg,
    }
    return render(request, "shipping/shipping.html", context)

def product(request, product_id=False, product_slug=False):
   
    if product_id:
        product = Products.objects.get(id=product_id)
    else:
        product = Products.objects.get(slug=product_slug)

    context = {
       'product': product
    }
    return render(request, "shipping/product.html", context=context)
