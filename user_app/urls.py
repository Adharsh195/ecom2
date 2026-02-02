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
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register_user',views.Register_user,name='Regiester_user'),
    # path('login_user',views.login_user,name='login_user'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('session_login',views.session_login,name="session_login"),
    path('session_dashboard',views.session_dashboard,name="session_dashboard"),
]
