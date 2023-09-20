from django import forms
from .models import Reserva
from django.forms import ModelForm

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria_empresa': forms.Select(attrs={'class': 'form-control'}),
            'quitado': forms.CheckboxInput(),  
            'stand': forms.Select(attrs={'class': 'form-control'}),          
        }
