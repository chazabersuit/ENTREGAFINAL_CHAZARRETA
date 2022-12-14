from django.urls import path
from .views import crear_post, inicio, listado, editar, eliminar, sobrenosotros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobrenosotros', sobrenosotros, name='sobrenosotros'),
    path('crear_post/',crear_post, name='crear_post'),
    path('listado/',listado, name='listado'),
    path('editar/<int:id>/',editar, name='editar'),
    path('eliminar/<int:id>/',eliminar, name='eliminar'),
]