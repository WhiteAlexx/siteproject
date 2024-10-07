from django.contrib import admin
from goods.models import Categories, Products

# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    save_on_top = True
    save_as = True

    prepopulated_fields = {'slug': ('name',)}

    list_display = ['name', 'quantity', 'unit', 'is_neo']
    list_editable = ['quantity', 'is_neo']

    search_fields = ['name', 'description']
    list_filter = ['unit', 'category', 'is_neo']

    fields = [
        ('name', 'slug'),
        ('category', 'is_neo'),
        ('price', 'count_for', 'discount'),
        ('price_mid', 'count_for_mid', 'discount_mid'),
        ('price_low', 'count_for_low', 'discount_low'),
        ('quantity', 'unit'),
        'description',
        ('image', 'image_1', 'image_2'),
        ('residual', 'is_residual'),
    ]
