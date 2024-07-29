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

    # list_display = ['name', 'unit', 'count_for_mid', 'count_for_low']
    # list_editable = ['unit', 'count_for_mid', 'count_for_low']

    # list_display = ['name', 'price', 'price_mid', 'count_for_mid', 'price_low', 'count_for_low']
    # list_editable = ['price', 'price_mid', 'count_for_mid', 'price_low', 'count_for_low']

    list_display = ['name', 'quantity', 'unit', 'price', 'discount']
    list_editable = ['price', 'discount', 'quantity',]

    search_fields = ['name', 'description']
    list_filter = ['unit', 'discount', 'category']
    fields = [
        ('name', 'slug'),
        'category',
        ('price', 'discount'),
        ('price_mid', 'count_for_mid'),
        ('price_low', 'count_for_low'),
        ('quantity', 'unit'),
        'description',
        'image',
    ]
