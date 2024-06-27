
from django.urls import path

from shipping import views

app_name = 'shipping'

urlpatterns = [
    path('', views.ShippingView.as_view(), name='index'),
    path('<int:page>/', views.ShippingView.as_view(), name='index'),
    # path('shipping/<int:product_id>/', views.product, name='product'),
    path('shipping/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
]