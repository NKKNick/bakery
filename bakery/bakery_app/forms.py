from django import forms
from .models import Product

class BakeryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'amount', 'descriptions', 'category', 'image']