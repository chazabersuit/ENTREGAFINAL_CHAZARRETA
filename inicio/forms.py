from django import forms

class CrearPost(forms.Form):
    nombre=forms.CharField(max_length=15)
    subtitulo=forms.CharField(max_length=30)
    contenido=forms.CharField(max_length=100)