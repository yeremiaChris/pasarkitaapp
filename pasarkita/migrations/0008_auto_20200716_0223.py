# Generated by Django 3.0.8 on 2020-07-16 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasarkita', '0007_barang_deskripsi2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='kategori',
            field=models.CharField(choices=[('Daging', 'Daging'), ('Sayur', 'Sayur'), ('Bumbu', 'Bumbu'), ('Bawang', 'Bawang'), ('Cabe', 'Cabe'), ('Buah', 'Buah'), ('Peralatan', 'peralatan')], default='Sayur', max_length=200),
        ),
    ]
