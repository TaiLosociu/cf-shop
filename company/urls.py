from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('base.html', views.newsletter, name='newsletter'),
    path('about/', views.about.as_view(), name='about'),
]
