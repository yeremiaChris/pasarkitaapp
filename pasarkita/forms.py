from django import forms

from .models import Image



# class ImageForm(forms.Form):
#     image = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'sampul','onchange': 'previewImg()'}))

class TambahBarangForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'id': 'sampul', 'onchange': 'previewImg()'})
        }
