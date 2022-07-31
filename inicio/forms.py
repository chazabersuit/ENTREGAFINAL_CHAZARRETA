from django import forms

class CrearPost(forms.Form):
    titulo=forms.CharField(max_length=15)
    subtitulo=forms.CharField(max_length=30)
    contenido=forms.CharField(max_length=100)
    
class Busqueda(forms.Form):
    titulo=forms.CharField(max_length=15,required=False)