from django.contrib import admin
from .models import Product

admin.site.register(Product)
admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
