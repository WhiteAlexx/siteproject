from django.urls import path

from favorites import views

app_name = "favorites"

urlpatterns = [
    path("favorite_add/", views.FavoriteAddView.as_view(), name="favorite_add"),
    path("favorite_del/", views.FavoriteDelView.as_view(), name="favorite_del"),
]
