from django.urls import path

from accounts.views import login,register, perfil, editar_perfil
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('perfil/', perfil , name='perfil'),
    path('register/', register, name='register'),
    path('editar_perfil/', editar_perfil, name='editar_perfil')
]