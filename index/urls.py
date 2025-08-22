from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('services', views.services, name='services'),
]
