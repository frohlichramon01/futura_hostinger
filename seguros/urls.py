from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('auto/', views.auto, name="auto"),
    path('vida/', views.vida, name="vida"),
    path('casa/', views.casa, name="casa"),
    path('empresa/', views.empresa, name="empresa"),
    path('viagem/', views.viagem, name="viagem"),
    path('sobre/', views.sobre, name="sobre"),
]
