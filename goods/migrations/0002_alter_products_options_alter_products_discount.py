# Generated by Django 4.2.11 on 2024-03-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %'),
        ),
    ]
