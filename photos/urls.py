from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name='home'),
    path('Obras', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]