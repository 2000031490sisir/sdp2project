from . import views
from django.urls import path

urlpatterns = [
    #path('/', views.index, name='index'),
    path('', views.homescreen),
    path('', views.homescreencss),
    path('home/', views.home),
    path('home/', views.homescreencss),
    path('login/', views.login),
    path('newuser/', views.newuser),
    path('login/', views.validations),
    path('newuser/', views.validations),
    path('login/', views.bfspython),
    path('contact/', views.contact),
    path('about/', views.about),
]
