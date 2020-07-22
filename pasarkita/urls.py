from django.urls import path
from django.contrib.auth import views as view
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.register,name='register'),
    path('tambah-barang', views.tambahBarang,name='tambah-barang'),
]
 