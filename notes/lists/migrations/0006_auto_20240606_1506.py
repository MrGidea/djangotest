# Generated by Django 3.0 on 2024-06-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20240606_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='List',
            new_name='list',
        ),
    ]
