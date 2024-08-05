from django.db import models

from goods.models import Products
from users.models import User


class OrderitemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    telnmbr = models.DecimalField(max_digits=11, decimal_places=0, verbose_name="Номер телефона")
    adres = models.CharField(max_length=250, null=True, blank=True, verbose_name="Адрес доставки")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default='Ожидает оплаты',
                              choices=(('Ожидает оплаты', 'Ожидает оплаты'),
                                       ('В обработке', 'В обработке'),
                                       ('Собран', 'Собран'),
                                       ('В пути', 'В пути'),
                                       ('Доставлено', 'Доставлено'),
                                       ),
                              verbose_name="Статус заказа")
    total_cost = models.DecimalField(default=0.00, max_digits=11, decimal_places=2, verbose_name="Стоимость")

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Товар", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Количество")
    unit = models.CharField(max_length=10, blank=True, null=True, verbose_name='Единица измерения')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        if self.order.user.groups.name == 'Опт':
            return round(self.product.sell_price_low() * self.quantity, 2)
        if self.quantity >= self.product.count_for_mid:
            return round(self.product.sell_price_mid() * self.quantity, 2)
        if self.quantity < self.product.count_for_mid:
            return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} | Заказ № {self.order.pk}"
