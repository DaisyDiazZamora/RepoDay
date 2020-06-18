"""from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
]"""
from django.conf.urls import url
from django.urls import path
from . import views
from . import casilla
from . import candidato, funcionario, rol
urlpatterns = [
#CASILLA
 path('casilla/listar', casilla.listar, name='listar'),
 path('casilla/add', casilla.add),
 path('casilla/delete/<int:casilla_id>', casilla.delete), 
 path('casilla/edit/<int:casilla_id>', casilla.edit), 
#FUNCIONARIO
path('funcionario/listar', funcionario.listar, name='listar'),
path('funcionario/add', funcionario.add),
path('funcionario/edit/<int:funcionario_id>', funcionario.edit), 
path('funcionario/delete/<int:funcionario_id>', funcionario.delete),
#ROL
path('rol/listar', rol.listar, name='listar'),
path('rol/add', rol.add),
path('rol/edit/<int:rol_id>', rol.edit), 
path('rol/delete/<int:rol_id>', rol.delete),

]

