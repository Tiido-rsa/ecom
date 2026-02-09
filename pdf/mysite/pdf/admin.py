from django.contrib import admin
from .models import Profile

admin.site.site_header  = "PDF Generator Admin"
admin.site.site_title   = "PDF Generator Admin Portal"
admin.site.index_title  = "Welcome to the PDF Generator Admin Portal"
admin.site.register(Profile)