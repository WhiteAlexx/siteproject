# Generated by Django 4.2.11 on 2024-04-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В обработке', 'В обработке'), ('В пути', 'В пути'), ('Доставлено', 'Доставлено')], default='В обработке', max_length=50, verbose_name='Статус заказа'),
        ),
    ]
