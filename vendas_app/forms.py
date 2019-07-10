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
    def clean_numero(self):
        numero = self.cleaned_data['numero']

        if numero:
            venda = NotaFiscal.objects.filter(numero=numero).exists()

            if venda:
                raise forms.ValidationError('Já existe uma venda cadastrada com esse código')
            return venda