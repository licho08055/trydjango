from django.db import models
from django.urls import reverse


class Article(models.Model):
    name = models.CharField(max_length=100)
    option = models.CharField(max_length=100)
    active = models.BooleanField()
    
    
                
    def get_absolute_url(self):
       return reverse('articles:detail', kwargs={'id': self.id})
