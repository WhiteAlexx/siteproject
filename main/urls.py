from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("delivery/", views.DeliveryView.as_view(), name="delivery"),
    # path("payment/<int:order_id>/", views.payment, name="payment"),
]
