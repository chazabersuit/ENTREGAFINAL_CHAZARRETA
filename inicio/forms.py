from django import forms
from ckeditor.fields import RichTextFormField

class CrearPost(forms.Form):
    titulo=forms.CharField(max_length=15)
    subtitulo=forms.CharField(max_length=30)
    contenido=RichTextFormField()
    
    
class Busqueda(forms.Form):
    titulo=forms.CharField(max_length=15,required=False,label='Buscar por titulo de post')