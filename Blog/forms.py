from django import forms
from .models import Post

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    cuerpo = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=100)
    fecha = forms.DateField()
    imagen = forms.ImageField()