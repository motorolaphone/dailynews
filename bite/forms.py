from django.forms import ModelForm
from . models import contact

class contactform(ModelForm):
	class Meta:
		model = contact
		fields = '__all__'