# Generated by Django 3.0 on 2024-06-06 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='list',
            new_name='List',
        ),
    ]
