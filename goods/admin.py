from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

#admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'unit', 'price', 'discount']
    list_editable = ['discount', 'quantity',]
    search_fields = ['name', 'description']
    list_filter = ['unit', 'discount', 'category']
    fields = [
        ('name', 'slug'),
        'category',
        ('price', 'discount'),
        ('quantity', 'unit'),
        'description',
        'image',
    ]
