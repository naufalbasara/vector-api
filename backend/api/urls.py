from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductList.as_view()), #get list of product
    path('products/<int:pk>/', views.product_detail), #detail of product, update, delete
    path('products/create/', views.handling_data), #create product
    path('send/', views.send_email), #send email
]