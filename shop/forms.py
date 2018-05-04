from django import forms

from .models import Book

class ShopForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title','author','price','ISBN','comment','document')