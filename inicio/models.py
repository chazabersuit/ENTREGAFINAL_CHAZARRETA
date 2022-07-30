from statistics import mode
from django.db import models
from pkg_resources import require

# Create your models here.
class Blog(models.Model):
    titulo= models.CharField(max_length=15)
    subtitulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=100)