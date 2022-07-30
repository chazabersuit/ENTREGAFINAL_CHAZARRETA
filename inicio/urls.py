from django.urls import path
from .views import crear_post, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear_post/',crear_post, name='crear_post')
]