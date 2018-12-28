from django.forms import ModelForm
from . models import ClienteBD

class clienteForm(ModelForm):
	class Meta:
		model = ClienteBD
		fields = '__all__'




"""
from django.forms import ModelForm
from . models import ClienteBD

class clienteForm(ModelForm):
	class Meta:
		model = ClienteBD

		fields = '__all__'
"""