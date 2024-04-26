from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products
from goods.utils import q_search


# Create your views here.
def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "tovary":
        goods = Products.objects.exclude(category__slug__icontains='v-puti').exclude(category__slug__icontains='udalennye')
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6)
    crrnt_pg = paginator.page(page)

    print(crrnt_pg.object_list)

    context = {
        "title": "Товары в наличии",
        "goods": crrnt_pg,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_id=False, product_slug=False):

    if product_id:
        product = Products.objects.get(id=product_id)
    else:
        product = Products.objects.get(slug=product_slug)

    context = {"product": product}
    return render(request, "goods/product.html", context=context)
