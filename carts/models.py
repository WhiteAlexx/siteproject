from django.db import models
from django.forms import BooleanField

from goods.models import Products
from users.models import User

# Create your models here.
class CartQueryset(models.QuerySet):

    def total_price(self):
        carts = Cart.objects.filter(select_buy='True')
        return sum(cart.products_price() for cart in carts)

    def select_quantity(self):
        if self:
            carts = Cart.objects.filter(select_buy='True')
            return sum(cart.quantity for cart in carts)

        return 0

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)

        return 0

class Cart(models.Model):

    select_buy = models.BooleanField(default=True, verbose_name='VX')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name='Корзина'
        verbose_name_plural='Корзина'
        ordering = ('id',)

    objects = CartQueryset().as_manager()

    def products_price(self):
        if self.quantity < self.product.count_for_mid:
            return round(self.product.sell_price() * self.quantity, 2)
        if self.quantity >= self.product.count_for_mid:
            return round(self.product.price_mid * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username}{self.select_buy} | Товар {self.product.name} | Количество {self.quantity} | {self.product.unit}'

        return f'Анонимная корзина{self.select_buy} | Товар {self.product.name} | Количество {self.quantity} | {self.product.unit}'
