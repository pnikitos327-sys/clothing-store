from django.urls import path
from . import views
from .views import registersion_view

urlpatterns = [
    path('', registersion_view, name='register'),
    path('1', views.home, name='home'),
    path('cart/', views.cart_view, name='cart'),  
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]