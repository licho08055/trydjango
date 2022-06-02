from dataclasses import fields
from django import forms
from .models import Blog
from django.shortcuts import HttpResponseRedirect

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
        ]
        
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError('This is not a valid title')
        return title
    
    
    
    
    
    
     