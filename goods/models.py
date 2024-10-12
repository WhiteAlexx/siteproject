from django.db import models
from django.urls import reverse


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    image = models.ImageField(upload_to="cats_images", blank=True, null=True, verbose_name="Изображение")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name="Категория")
    is_neo = models.BooleanField(default=True, verbose_name='В новинки')
    created_time_stamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    price = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name="Цена")
    count_for = models.IntegerField(default=1, verbose_name="Минимум единиц товара")
    discount = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name="Скидка в %")

    price_mid = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name="Цена мелкий опт")
    count_for_mid = models.IntegerField(default=1, verbose_name="Единиц товара для мелкого опта")
    discount_mid = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name="Скидка в %")

    price_low = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name="Цена опт")
    count_for_low = models.IntegerField(default=1, verbose_name="Единиц товара для опта")
    discount_low = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name="Скидка в %")

    unit = models.CharField(max_length=10, verbose_name="Единица измерения")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Изображение 1")
    image_1 = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Изображение 2")
    image_2 = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Изображение 3")

    is_residual = models.BooleanField(default=False, verbose_name='В остатках')
    residual = models.CharField(max_length=100, blank=True, null=True, verbose_name="Остатки (ЦЕЛЫЕ, вносить через ПРОБЕЛ)")

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.name} Количество: {self.quantity} {self.unit}"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def sell_price_mid(self):
        if self.discount_mid:
            return round(self.price_mid - self.price_mid * self.discount_mid / 100, 2)
        return self.price_mid

    def sell_price_low(self):
        if self.discount_low:
            return round(self.price_low - self.price_low * self.discount_low / 100, 2)
        return self.price_low

    def residual_list_float(self):
        if ',' in  self.residual:
            self.residual =  self.residual.replace(',', '.')
        return [int(y) for y in self.residual.split()]

    def residual_list(self):
        if ',' in  self.residual:
            self.residual =  self.residual.replace(',', '.')
        return [str(int(y)) for y in self.residual.split()]

    def residual_cost_low(self):
        return {[int(y) for y in self.residual_list()] : [int(self.sell_price_low()) * int(i) for i in self.residual_list()]}
