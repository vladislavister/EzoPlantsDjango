# Generated by Django 4.1.3 on 2022-11-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='static/media/products_images/'),
        ),
    ]
