
from tkinter import EW
from django.shortcuts import redirect, render

from .models import Blog
from .forms import Busqueda, CrearPost

# Create your views here.
def inicio(request):
    
    return render(request,'inicio/inicio.html',{})

def crear_post(request):
    form=CrearPost()
    
    if request.method== 'POST':
        form=CrearPost(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            post=Blog(
                titulo=data.get('titulo').upper(),
                subtitulo=data.get('subtitulo').lower(),
                contenido=data.get('contenido'),
                )
            post.save()
            listado=Blog.objects.all()
            return redirect('listado')
           
    else:
         return render(request,'inicio/blog.html',{'form':form})
         
    return render(request,'inicio/blog.html',{'form':form})

def listado(request):
    form=Busqueda()
    busqueda=request.GET.get('titulo')
    if busqueda:
        listado=Blog.objects.filter(titulo__icontains=busqueda)
    else:
        listado=Blog.objects.all()
    return render(request,'inicio/listado.html',{'listado':listado,'form':form})

def editar(request,id):
    dato=Blog.objects.get(id=id)
    form=CrearPost(initial={'titulo':dato.titulo,'subtitulo':dato.subtitulo,'contenido':dato.contenido})
    
    if request.method=="POST":
        form=CrearPost(request.POST)
        if form.is_valid():
            dato.titulo=form.cleaned_data.get('titulo')
            dato.subtitulo=form.cleaned_data.get('subtitulo')
            dato.contenido=form.cleaned_data.get('contenido')
            print('pase por 1')
            dato.save()
            return redirect('listado')
        else:
            print('pase por 2')
            return render(request,'inicio/blog.html',{'dato':dato})
    print('pase por 3')
    return render(request,'inicio/editar.html',{'form':form,'dato':dato})


def eliminar(request,id):
    dato=Blog.objects.get(id=id)
    dato.delete()
    return redirect('listado')

def mostrar(request,id):
    dato=Blog.objects.get(id=id)
    return render(request,'inicio/listado.html',{'dato':dato})