"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('list_items/',views.list_items,name='list_items'),
    path('add_items/',views.add_items,name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('accounts/', include('registration.backends.default.urls')),
    path('list_history/', views.list_history, name='list_history'),
    path('accounts/', include('allauth.urls')),
    path('list_itemss/',views.list_itemss,name='list_itemss'),
]