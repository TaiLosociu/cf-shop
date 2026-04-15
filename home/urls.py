from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('auth/', views.auth_page, name='auth_page'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
