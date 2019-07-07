from django.shortcuts import render,redirect,get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_produtos(request):
    produtos = Produto.objects.all().filter(user=request.user)
    return render(request, 'produtos/produto/listar.html',{'produtos':produtos})

@login_required
def adicionar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        produto = form.save(commit=False)
        produto.user= request.user
        produto.save()
        form = ProdutoForm()
    return render(request, 'produtos/produto/adicionar.html', {'form': form})

@login_required
def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
    return render(request, 'produtos/produto/adicionar.html', {'form': form})

@login_required
def detalhar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/produto/detalhar.html', {'produto': produto})

@login_required
def remover_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('produtos:listar')
