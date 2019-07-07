from django import forms
from .models import Cliente


class ClienteNovoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'email',
            'nome'
        ]