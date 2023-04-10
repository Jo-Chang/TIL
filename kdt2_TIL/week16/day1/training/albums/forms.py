from .models import Album
from django import forms

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'content': '내용',
            'image': '사진',
        }
        widgets = {
            'content': forms.TextInput(attrs={'class':'form-control custom-input-content-form',}),
            'image': forms.FileInput(attrs={'class':'form-control custom-input-content-form',}),
        }