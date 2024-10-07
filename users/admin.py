from django.contrib import admin

# Register your models here.
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'telnmbr',]
    search_fields = ['last_name', 'first_name', 'telnmbr', 'username',]

    inlines = [CartTabAdmin, OrderTabulareAdmin,]
