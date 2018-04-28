from django import forms

from .models import OrdItem

class OrdForm(forms.ModelForm):

    class Meta:
        model = OrdItem
        fields = ('first','last','email','phone')