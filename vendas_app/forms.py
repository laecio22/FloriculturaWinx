from django import forms
from .models import NotaFiscal

class EfetuarVendaForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = [
            'numero',
            'cliente',
            'item'
        ]