# Generated by Django 3.0.8 on 2020-07-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasarkita', '0017_images_barang'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]