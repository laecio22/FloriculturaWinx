from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):

    class Meta:
        model= Produto
        fields =[
            'nome',
            'codigo',
            'descricao'
        ]

    def clean_codigo(self):
         codigo = self.cleaned_data['codigo']

         if codigo :
             produto = Produto.objects.filter(codigo=codigo).exists()

             if produto :
                  raise forms.ValidationError('Já existe um produto cadastrado com esse código')

             return produto

