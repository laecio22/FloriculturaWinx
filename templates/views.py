from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def principal(request):
    return render(request, 'index2.html')

def sobre(request):
    return render(request, 'sobre.html' )

def contato(request):
    return render(request,'contato2.html' )

@login_required
def home(request):
    return render(request, 'home.html')