from django.shortcuts import render, redirect, get_object_or_404
from .models import NotaFiscal
from .forms import EfetuarVendaForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_vendas(request):
    vendas = NotaFiscal.objects.all().filter(user=request.user)
    return render(request, 'vendas/venda/listar.html', {'vendas': vendas})

@login_required
def efetuar_venda(request):
    form = EfetuarVendaForm(request.POST or None)
    if form.is_valid():
        venda = form.save(commit=False)
        venda.user = request.user
        venda.save()
        form = EfetuarVendaForm()
    return render(request, 'vendas/venda/efetuar_venda.html', {'form': form})

@login_required
def atualizar_venda(request, id):
    venda = get_object_or_404(NotaFiscal, id=id)
    form = EfetuarVendaForm(request.POST or None,instance=venda )
    if form.is_valid():
        form.save()
    return render(request, 'vendas/venda/efetuar_venda.html', {'form': form})

@login_required
def detalhar_venda(request, id):
    venda = get_object_or_404(NotaFiscal, id=id)
    return render(request, 'vendas/venda/detalhar.html', {'venda': venda})

@login_required
def remover_venda(request, id):
    venda = NotaFiscal.objects.get(id=id)
    venda.delete()
    return redirect('vendas:listar_vendas')