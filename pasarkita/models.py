from django.db import models
from django.conf import settings

# Create your models here.


class Barang(models.Model):
    image = models.FileField(upload_to='gambar/')
    nama = models.CharField(max_length=200,default='Produk')
    deskripsi = models.TextField(max_length=500,default='keterangan')
    deskripsi2 = models.TextField(max_length=500,default='keterangan')
    CATEGORY = (
        ('Daging', 'Daging'),
        ('Sayur', 'Sayur'),
        ('Bumbu', 'Bumbu'),
        ('Bawang', 'Bawang'),
        ('Cabe', 'Cabe'),
        ('Buah', 'Buah'),
        ('Peralatan', 'peralatan'),
    )
    kategori  = models.CharField(max_length=200,choices=CATEGORY,default='Sayur')
    harga = models.IntegerField(default=0)

