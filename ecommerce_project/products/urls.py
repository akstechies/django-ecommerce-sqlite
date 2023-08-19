from django.urls import path
from . import views

app_name = 'products'  # This is important to avoid URL conflicts

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('tags/', views.tag_list, name='tag_list'),
    path('tags/create/', views.tag_create, name='tag_create'),
    path('tags/update/<int:pk>/', views.tag_update, name='tag_update'),
    path('tags/delete/<int:pk>/', views.tag_delete, name='tag_delete'),

    path('view_list/', views.view_product_list, name='view_product_list'),
    path('view_detail/<int:pk>/', views.view_product_detail, name='view_product_detail')
]
