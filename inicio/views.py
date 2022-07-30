from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    
    return render(request,'inicio/inicio.html',{})

def blog(request):
    return render(request,'inicio/blog.html')