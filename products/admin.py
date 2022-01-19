from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        
        'name',
        'price',
        'is_service',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
