# Generated by Django 3.1.1 on 2020-09-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200729_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_icon',
            field=models.ImageField(upload_to='images/'),
        ),
    ]