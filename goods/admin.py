from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

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

#     def response_add(self, request, obj, post_url_continue=None):
#         if post_url_continue is None:
#             post_url_continue = get_success_url(request)
#         return HttpResponseRedirect(post_url_continue)

#     def response_change(self, request, obj):
#         return HttpResponseRedirect(get_success_url(request))

#     def response_delete(self, request, obj_display, obj_id):
#         return HttpResponseRedirect(get_success_url(request))

# def get_success_url(request):
#     redirect_page = request.path
#     print(redirect_page)
#     if redirect_page:
#         return redirect_page
#     # return reverse_lazy("/admin/goods/products/")
