# Generated by Django 4.2.11 on 2024-07-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_products_count_for_mid_products_price_low_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='count_for_low',
            field=models.DecimalField(decimal_places=2, default=150, max_digits=7, verbose_name='Единиц товара для опта'),
        ),
        migrations.AlterField(
            model_name='products',
            name='count_for_mid',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=7, verbose_name='Единиц товара для мелкого опта'),
        ),
    ]
