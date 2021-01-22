from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:categoryid>', views.ProductInCategory.as_view()),
    path('products_list/', views.products_list.as_view()),
    path('products_info/', views.products_info.as_view()),
    path('products_info/detail/', views.get_products_info),
    path('products_list_ajax/', views.products_list_ajax.as_view()),
    path('products_list_ajax/detail/', views.get_products_list_ajax, name = 'prod_list')
]