from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
     path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]