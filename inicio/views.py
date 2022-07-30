from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from inicio.forms import CrearPost

# Create your views here.
def inicio(request):
    
    return render(request,'inicio/inicio.html',{})

def crear_post(request):
    
    if request.method== 'POST':
        form=CrearPost(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            fecha=data.get('fecha_creacion')
            post=CrearPost(
                titulo= data.get('titulo'),
                subtitulo=data.get('subtitulo'),
                contenido=data.get('comentario'),
                fecha_creacion= fecha if fecha else datetime.now()
            )
            post.save()
    
    form=CrearPost()
    
    return render(request,'inicio/blog.html',{'form':form})