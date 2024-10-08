# Generated by Django 4.2.11 on 2024-08-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_products_image_1_products_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='residual_5',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Остаток'),
        ),
        migrations.AddField(
            model_name='products',
            name='residual_6',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение 3'),
        ),
    ]
