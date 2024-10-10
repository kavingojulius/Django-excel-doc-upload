from django.forms import ModelForm
from .models import Items

class AddForm(ModelForm):

    class Meta:

        model = Items
        
        fields = '__all__'