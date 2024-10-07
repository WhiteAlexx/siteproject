from django.urls import path

from carts import views

app_name = "carts"

urlpatterns = [
    path("cart_add/", views.CartAddView.as_view(), name="cart_add"),
    path("cart_add_mid/", views.CartAddMidView.as_view(), name="cart_add_mid"),
    path("cart_add_low/", views.CartAddLowView.as_view(), name="cart_add_low"),
    path("cart_change/", views.CartChangeView.as_view(), name="cart_change"),
    path("cart_remove/", views.CartRemoveView.as_view(), name="cart_remove"),
    path("cart_select/", views.cart_select, name="cart_select"),
]
