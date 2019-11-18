from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),
    path('Index.html', views.Index, name='Index'),
    path('RegistroUsuario.html', views.RegistroUsuario, name='RegistroUsuario')

]