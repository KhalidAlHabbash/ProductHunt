# Generated by Django 3.0.8 on 2020-07-29 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200729_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_hunter',
            new_name='hunter',
        ),
    ]
