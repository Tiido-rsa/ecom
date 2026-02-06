from django.contrib import admin
from .models import Order, Product, Wishlist

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
