from django.shortcuts import render,redirect

from . models import Image



from . forms import TambahBarangForm






# Create your views here.
def index(request):
    return render(request,'pasarkita/index.html')


def tambahBarang(request): 
    form = TambahBarangForm()

    if request.method == 'POST':
        form = TambahBarangForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
        return redirect('tambah-barang')

    context = {
        'form': form,
    }
    return render(request,'pasarkita/tambah-barang.html',context)
