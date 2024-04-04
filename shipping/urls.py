
from django.urls import path

from shipping import views

app_name = 'shipping'

urlpatterns = [
    path('', views.shipping, name='index'),
    path('<int:page>/', views.shipping, name='index'),
    path('shipping/<int:product_id>/', views.product, name='product'),
    path('shipping/<slug:product_slug>/', views.product, name='product'),
]