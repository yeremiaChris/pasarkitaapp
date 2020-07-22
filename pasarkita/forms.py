from django import forms
from .models import Barang
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class TambahBarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama', 'deskripsi','deskripsi2', 'kategori', 'harga','alamat','alamat2','image']
        widgets = {
            # 'image': forms.ClearableFileInput(attrs={'id': 'sampul', 'onchange': 'previewImg()'}),
            'deskripsi': forms.Textarea(attrs={'id': 'satu','cols': '50','rows':'10'}),
            'deskripsi2': forms.Textarea(attrs={'id': 'dua','cols': '117','rows':'15'}),
            'alamat': forms.Textarea(attrs={'id': 'satu','cols': '50','rows':'10'}),
            'alamat2': forms.Textarea(attrs={'id': 'dua','cols': '117','rows':'15'}),
            'kategori': forms.Select(attrs={'class':'js-example-basic-single','name':'kategori'})
        }

class registerForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email','password1','password2','username']
    def __init__(self, *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 're-password'


        
