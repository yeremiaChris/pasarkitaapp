from django.shortcuts import render,redirect


from .models import Images
from . forms import TambahBarangForm
from django.forms import modelformset_factory
from django import forms










# Create your views here.
def index(request):
    return render(request,'pasarkita/index.html')


def tambahBarang(request): 
    form = TambahBarangForm()
    ImageFormSet = modelformset_factory(Images,fields=['images'],extra=2,widgets={
        'images': forms.ClearableFileInput(attrs={'id': 'sampul'})
    })
    if request.method == 'POST':
        form = TambahBarangForm(request.POST or None,request.FILES or None)
        formset = ImageFormSet(request.POST or None,request.FILES or None)
        if form.is_valid() and formset.is_valid():
            barang = form.save()

            for f in formset:
                try:
                    photo = Images(barang=barang,images=f.cleaned_data['images'])
                    photo.save()
                except expression as identifier:
                    pass
            return redirect('index')
    else:
        form = TambahBarangForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    context = {
        'form': form,
        'formset':formset
    }
    return render(request,'pasarkita/tambah-barang.html',context)
