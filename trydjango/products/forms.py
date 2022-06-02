from logging import PlaceHolder
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
     title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Your title'}) )
     description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Your description'}))
     price = forms.DecimalField(initial=199.99)
     class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
        
     def clean_title(self):
         title = self.cleaned_data.get('title')
         if not 'emma' in title:
             raise forms.ValidationError('Not your name')
         return title
        
        
        
        
        
        
class  RawProductForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Your title'}) )
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Your description'}))
    price = forms.DecimalField(initial=199.99)
    
    
    
    
    
    