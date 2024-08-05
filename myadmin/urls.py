from django.contrib.auth import views as auth_views
from django.urls import path

from myadmin import views

app_name = "myadmin"

urlpatterns = [
    path("", views.MyAdminView.as_view(), name="myadmin"),
    path("order_done/", views.orderdone, name="order_done"),
]
