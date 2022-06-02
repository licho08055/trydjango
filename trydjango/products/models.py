from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    
    
    def get_absolute_url(self):
        return f"/products/{self.id}/"
