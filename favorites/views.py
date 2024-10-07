from django.http import JsonResponse
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

        if not favorite:
            Favorite.objects.create(user=request.user if request.user.is_authenticated else None,
                                    session_key=request.session.session_key if not request.user.is_authenticated else None,
                                    product=product)

        response_data = {
            "message": f"{product.name} добавлен в избранное",
        }

        return JsonResponse(response_data)


class FavoriteDelView(View):

    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        favorite = get_favorite(request, product=product)

        if favorite:
            favorite.delete()

        response_data = {
            "message": f"{product.name} удалён из избранного",
        }

        return JsonResponse(response_data)
