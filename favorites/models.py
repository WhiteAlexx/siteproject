from django.db import models

# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to='goods.Products', on_delete=models.CASCADE, verbose_name='Товар')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'favorite'
        verbose_name='Избранное'
        verbose_name_plural='Избранное'
        ordering = ('-created_timestamp',)

    def __str__(self):
        if self.user:
            return f'{self.user.username} - {self.product.name}'
        else:
            return f'{self.session_key} - {self.product.name}'
