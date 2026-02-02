"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('order_list',views.order_list,name='order_list'),
    path('user_list',views.user_list,name='user_list'),
    path('orders_details',views.orders_details,name='order_details'),
    path('cart_details',views.cart_details,name='cart_details'),
    path('cart_items',views.cart_items,name='cart_items'),
    path('delete_item',views.delete_item,name='delete_item'),
    path('admin/', admin.site.urls),
    # path('Register_user',views.Register_user,name='Regiester_user'),
    # path('login_user',views.login_user,name='login_user'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('firstpage',views.firstpage,name='firstpage'),
    path("cart/", views.view_cart, name="view_cart"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add-to-cart"),
]


