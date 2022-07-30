from django.urls import path
from .views import inicio, blog

urlpatterns = [
    path('', inicio, name='inicio'),
    path('blog/',blog, name='blog')
]