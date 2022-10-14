from django.contrib import admin

# Register your models here.

from .models import Product, ContactUs


admin.site.register(Product)
admin.site.register(ContactUs)