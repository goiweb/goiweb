from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    imageUrl = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=2000)
    ph_number = models.CharField(max_length=20, default="1234567890")

    def __str__(self):
        return self.email
