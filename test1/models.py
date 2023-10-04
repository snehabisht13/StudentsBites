from django.db import models
from django import forms


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=10000)
    price = models.FloatField(max_length=20)
    product_id = models.CharField(max_length=30,unique=True)
    img = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.product_id


# class PriceFilterForm(forms.Form):
#     min_price = forms.DecimalField(label='Min Price', required=False)
#     max_price = forms.DecimalField(label='Max Price', required=False)

class Contact(models.Model):
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.subject
