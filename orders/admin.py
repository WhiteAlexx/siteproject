from django.contrib import admin

from orders.models import Order, OrderItem

# Register your models here.

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = ("product", "name",)
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product_display", "name", "price", "quantity", "unit_display"
    search_filds = ("order", "product", "name",)

    def product_display(self, obj):
        return str(obj.product.name)

    def unit_display(self, obj):
        return str(obj.product.unit)


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = ("status", "created_timestamp",)

    search_fields = ("id", "created_timestamp",)
    readonly_fields = ("created_timestamp",)
    list_filter = ("status", "created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "status","created_timestamp",)
    list_editable = ['status']

    search_fields = ("id",)
    readonly_fields = ("created_timestamp",)
    list_filter = ("status",)

    inlines = (OrderItemTabulareAdmin,)

    def username(self, obj):
        
        return str(obj.user.last_name + ' ' + obj.user.first_name)
