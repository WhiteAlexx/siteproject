# from django.contrib.auth import views as auth_views
from django.urls import path

from myadmin import views

app_name = "myadmin"

urlpatterns = [
    path("search/", views.MyAdminView.as_view(), name="search"),
    path("order_done/", views.orderdone, name="order_done"),
    path("<slug:order_status>/", views.MyAdminView.as_view(), name="myadmin"),
    # path("goods/", views.MyAdminGoods.as_view(), name="goods"),
]
