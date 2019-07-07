from django .urls import path
from . import views

app_name = 'produtos'

urlpatterns =[
    path('produtos/',views.listar_produtos, name = 'listar'),
    path('produtos/adicionar/',views.adicionar_produto, name ='adicionar'),
    path('produtos/<int:id>/', views.detalhar_produto, name = 'detalhar'),
    path('produtos/<int:id>/atualizar', views.atualizar_produto, name ='atualizar'),
    path('produtos/<int:id>/remover',views.remover_produto, name = 'remover'),
    path('', views.listar_produtos, name = 'listar'),
]