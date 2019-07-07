from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('contato/', views.contato , name = 'contato'),
    path('home/', views.home, name='home'),
]