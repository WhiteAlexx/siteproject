

class CartMixin:
    def get_cart(self, request, product=None):
        if request.user.is_authenticated:
            query_kwargs = {'user': request.user}