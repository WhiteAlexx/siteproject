from favorites.models import Favorite

def get_favorite(request, product=None, favorite_id=None):
    if request.user.is_authenticated:
        query_kwargs = {'user': request.user}
    else:
        query_kwargs = {'session_key': request.session.session_key}

    if product:
        query_kwargs['product'] = product
    if favorite_id:
        query_kwargs['id'] = favorite_id
    return Favorite.objects.filter(**query_kwargs)
