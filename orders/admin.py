from django.contrib import admin

from orders.models import Order, OrderItem

# Register your models here.
# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = ("product", "name",)
    extra = 0

    # def unit_display(self, obj):
    #     return str(obj.product.unit)


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
    fields = ("status", "is_paid", "created_timestamp",)

    search_fields = ("id", "is_paid", "created_timestamp",)
    readonly_fields = ("created_timestamp",)
    list_filter = ("status", "is_paid", "created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status","created_timestamp",)
    list_editable = ['status']

    search_fields = ("id",)
    readonly_fields = ("created_timestamp",)
    list_filter = ("status", "is_paid",)

    inlines = (OrderItemTabulareAdmin,)
