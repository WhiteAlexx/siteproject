from django.urls import path

from carts import views

app_name = "carts"

urlpatterns = [
    path("cart_add/", views.cart_add, name="cart_add"),
    path("cart_change/", views.cart_change, name="cart_change"),
    path("cart_remove/", views.cart_remove, name="cart_remove"),
    path("cart_select/<slug:product_slug>/", views.cart_select, name="cart_select"),
    # path("cart_slctall/", views.cart_slctall, name="cart_slctall"),
]
