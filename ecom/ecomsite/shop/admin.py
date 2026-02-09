from django.contrib import admin
from .models import Order, Product, Wishlist


admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category='Default')
        
    change_category_to_default.short_description = "Change category to Default"
    list_display        = ('name', 'price', 'discount_price', 'category', 'image')
    search_fields       = ('name', 'category')
    list_filter         = ('category',)
    actions             = [change_category_to_default]
    fields              = ('name', 'description', 'price' )
    list_editable      = ('price', 'discount_price', 'category')

admin.site.index_title = "Welcome to the E-Commerce Admin Portal"

admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Product, ProductAdmin)