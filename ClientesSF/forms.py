from django.forms import ModelForm
from .models import Clientes

class ClientesForms(ModelForm):
    class Meta:
        model = Clientes
        fields = ['name', 'dni', 'email', 'address', 'phone', 'movil', 'avatar']