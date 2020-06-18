##def index(request):
 #return HttpResponse('Hola. bienvenido a django') 
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import CasillaForm

def casilla_new(request):
    form = CasillaForm()
    return render(request, '/casilla_edit.html', {'form': form})