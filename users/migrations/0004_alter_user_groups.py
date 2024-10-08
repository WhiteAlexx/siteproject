# Generated by Django 4.2.11 on 2024-08-03 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0003_remove_user_groups_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='auth.group', verbose_name='Группа'),
        ),
    ]
