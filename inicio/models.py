from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    titulo=models.CharField(max_length=15)
    subtitulo=models.CharField(max_length=30)
    contenido=RichTextField(null=True)
    autor=models.CharField(max_length=50)
    fecha_creacion=models.DateField(null=True)
    
    def __str__(self):
        return self.titulo