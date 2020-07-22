from django.shortcuts import render,redirect


from .models import Images,Barang
from . forms import TambahBarangForm,registerForm
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth import authenticate,login










# Create your views here.
def index(request):
    barang = Images.objects.all()
    context = {
        'barang': barang, 
    }
    return render(request,'pasarkita/index.html',context)


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
                    photo = Images(images=f.cleaned_data['images'])
                    photo.save()
                    
                except expression as identifier:
                    pass
            return redirect('index')
    else:
        form = TambahBarangForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    context = {
        'form': form,
        'formset':formset,
    }
    return render(request,'pasarkita/tambah-barang.html',context)


def register(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email,password=password)
            login(request,user)
        return redirect('login')
    context = {
        'form': form
    }
    return render(request,'registration/register.html',context)