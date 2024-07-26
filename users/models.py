from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True, null=True, verbose_name="Аватар")
    telnmbr = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True, verbose_name="Телефон")
    adres = models.CharField(max_length=250, blank=True, null=True, verbose_name="Адрес")
    groups = models.ForeignKey(to="auth.Group", blank=True, null=True, on_delete=models.PROTECT, verbose_name="Группа")

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
