# Generated by Django 4.2.11 on 2024-08-22 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
