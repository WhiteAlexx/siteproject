# Generated by Django 4.2.11 on 2024-07-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_products_count_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_time_stamp',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-02 00:00', verbose_name='Дата добавления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='discount_low',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %'),
        ),
        migrations.AddField(
            model_name='products',
            name='discount_mid',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %'),
        ),
        migrations.AddField(
            model_name='products',
            name='is_neo',
            field=models.BooleanField(default=True, verbose_name='В новинки'),
        ),
        migrations.AlterField(
            model_name='products',
            name='count_for_low',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Единиц товара для опта'),
        ),
    ]
