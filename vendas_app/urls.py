from django.urls import path
from . import views


app_name = 'vendas'

urlpatterns = [
    path('vendas/', views.listar_vendas, name='listar_vendas'),
    path('vendas/adicionar/', views.efetuar_venda, name='efetuar_venda'),
    path('vendas/<int:id>/', views.detalhar_venda, name='detalhar_venda'),
    path('vendas/<int:id>/atualizar', views.atualizar_venda, name='atualizar_venda'),
    path('vendas/<int:id>/remover', views.remover_venda, name='remover_venda'),
    path('', views.listar_vendas, name='listar_vendas'),
]