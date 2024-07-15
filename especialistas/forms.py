# usuario/forms.py

from django import forms
from .models import Especialista

class EspecialistaForm(forms.ModelForm):

    class Meta:
        model = Especialista
        fields = '__all__'
