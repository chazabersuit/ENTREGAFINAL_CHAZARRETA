from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo=models.CharField(max_length=15)
    subtitulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo