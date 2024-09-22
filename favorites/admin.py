from django.contrib import admin

from favorites.models import Favorite

# Register your models here.

class FavoriteTabAdmin(admin.TabularInline):
    model = Favorite
    fields = "product", "created_timestamp"
    search_fields = "product", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1

    def unit_display(self, obj):
        return str(obj.product.unit)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'created_timestamp',]
    # list_editable = ['product_display',]
    list_filter = ['user', 'created_timestamp',]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    def product_display(self, obj):
        return str(obj.product.name) + "-id-" + str(obj.product.id)

    def unit_display(self, obj):
        return str(obj.product.unit)

    # user_display and product_display alter name of columns in admin panel
    user_display.short_description = "Пользователь"
    product_display.short_description = "Товар"
