from django import forms
from .models import Cliente


class ClienteNovoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'email',
            'nome'
        ]
    def clean_email(self):

        email = self.cleaned_data['email']

        if email:
            cliente = Cliente.objects.filter(email=email).exists()

            if cliente:
                raise forms.ValidationError('Já existe um cliente cadastrado com esse email')
            return cliente