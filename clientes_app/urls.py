from django.urls import path
from . import views


app_name = 'clientes'

urlpatterns = [
    path('clientes/', views.listar_cliente, name='listar'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar'),
    path('clientes/<int:id>/', views.detalhar_cliente, name='detalhar'),
    path('clientes/<int:id>/atualizar', views.atualizar_cliente, name='atualizar'),
    path('clientes/<int:id>/remover', views.remover_cliente, name='remover'),
    path('', views.listar_cliente, name='listar'),
]