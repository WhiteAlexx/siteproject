# Generated by Django 4.2.11 on 2024-08-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_alter_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]