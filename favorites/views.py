from django.shortcuts import render
from django.views import View

from favorites.utils import get_favorite
from favorites.models import Favorite
from goods.models import Products

# Create your views here.

class FavoriteAddView(View):

    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        favorite = get_favorite(request, product=product)

        # if favorite:
        #     favorite.delete()
        if not favorite:
            Favorite.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product)

        return get_favorite(request)

class FavoriteDelView(View):

    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        favorite = get_favorite(request, product=product)

        if favorite:
            favorite.delete()

        return get_favorite(request)
