# Generated by Django 4.1.3 on 2022-11-30 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_productinbasket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinbasket',
            options={'verbose_name': 'Товар в корзині', 'verbose_name_plural': 'Товари y корзині'},
        ),
    ]
