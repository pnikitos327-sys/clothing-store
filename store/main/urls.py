from django.urls import path
from . import views
from .views import registersion_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('registersion/', registersion_view, name='register'),
    path('cart/', views.cart_view, name='cart'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('product/', views.product_delait, name='product')
]