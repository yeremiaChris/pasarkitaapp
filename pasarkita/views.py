from django.shortcuts import render,redirect



from . forms import TambahBarangForm






# Create your views here.
def index(request):
    return render(request,'pasarkita/index.html')


def tambahBarang(request): 
    form = TambahBarangForm()
    context = {
        'form': form
    }
    return render(request,'pasarkita/tambah-barang.html',context)
