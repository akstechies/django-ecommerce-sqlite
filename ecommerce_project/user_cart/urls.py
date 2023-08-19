# user_cart/urls.py

from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add_to_cart_ajax/', views.add_to_cart_ajax, name='add_to_cart_ajax'),
    path('remove_from_cart_ajax/', views.remove_from_cart_ajax, name='remove_from_cart_ajax'),
    path('view/', views.cart_view, name='cart_view')
]
