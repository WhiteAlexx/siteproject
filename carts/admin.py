from django.contrib import admin

from carts.models import Cart

# Register your models here.

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestamp"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1

    def unit_display(self, obj):
        return str(obj.product.unit)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display','select_buy', 'product_display', 'quantity', 'unit_display', 'created_timestamp',]
    list_editable = ['select_buy',]
    list_filter = ['user', 'product__name', 'created_timestamp',]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    def product_display(self, obj):
        return str(obj.product.name)

    def unit_display(self, obj):
        return str(obj.product.unit)

    # user_display and product_display alter name of columns in admin panel
    user_display.short_description = "Пользователь"
    product_display.short_description = "Товар"
