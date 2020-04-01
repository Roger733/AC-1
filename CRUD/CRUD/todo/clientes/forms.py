from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome', 'Modelo_Veiculo','Placa_Veiculo','tipo','email','profissao')
       