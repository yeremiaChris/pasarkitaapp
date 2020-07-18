from django import forms
from .models import Barang


class TambahBarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama', 'deskripsi','deskripsi2', 'kategori', 'harga']
        widgets = {
            # 'image': forms.ClearableFileInput(attrs={'id': 'sampul', 'onchange': 'previewImg()'}),
            'deskripsi': forms.Textarea(attrs={'id': 'satu','cols': '50','rows':'10'}),
            'deskripsi2': forms.Textarea(attrs={'id': 'dua','cols': '117','rows':'15'}),
            'kategori': forms.Select(attrs={'class':'js-example-basic-single','name':'kategori'})
        }

