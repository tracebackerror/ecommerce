from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'created_at','updated_at']
    readonly_fields = ['slug', 'created_at','updated_at']
    list_per_page = 20
    search_fields = ['title']
    filter_horizontal = ["images"]

admin.site.register(Address)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Cart)
admin.site.register(Order)
