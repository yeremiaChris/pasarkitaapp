from django.db import models
from django.conf import settings

# Create your models here.



class Barang(models.Model):
    nama = models.CharField(max_length=200,default='Produk')
    deskripsi = models.TextField(max_length=500,default='keterangan')
    deskripsi2 = models.TextField(max_length=500,default='keterangan')
    alamat = models.TextField(max_length=500,default='alamat')
    alamat2 = models.TextField(max_length=500,default='alamat')
    image = models.ImageField(default='default.png',upload_to='gambar')
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

    def __str__(self):
        return str(self.id)

class Images(models.Model):
    barang = models.ForeignKey(Barang,on_delete=models.CASCADE,null=True)
    images = models.ImageField(upload_to='gambar')
    def __str__(self):
        return str(self.id)