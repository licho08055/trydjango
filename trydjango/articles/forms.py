from dataclasses import fields
from django import forms
from django.shortcuts import reverse
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'name',
            'option',
            'active',
        ]
            
 