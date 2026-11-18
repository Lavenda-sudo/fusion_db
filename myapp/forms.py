from django import forms

from myapp.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields={'name', 'code', 'category', 'cost', 'price', 'for_sale', 'pic'}

