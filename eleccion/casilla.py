from django.http import HttpResponse
from .models import Casilla
from django.shortcuts import render
from .forms import CasillaForm
from django.shortcuts import redirect

def listar(request):
 lista_casilla = Casilla.objects.order_by('ubicacion')
 return render(request, 'casilla_listar.html',context= {'lista_casilla':lista_casilla})


def delete(request, casilla_id):
 # Recuperamos la instancia de la persona y la borramos
 eliminar_casilla = Casilla.objects.get(id=casilla_id)
 eliminar_casilla.delete()
 # Después redireccionamos de nuevo a la lista
 return redirect('/eleccion/casilla/listar')


def edit(request, casilla_id):
    # Recuperamos la instancia de la persona
    editar_casilla = Casilla.objects.get(id=casilla_id)

    # Creamos el formulario con los datos de la instancia
    form = CasillaForm(instance=editar_casilla)

    # Comprobamos si se ha enviado el formulario 
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = CasillaForm(request.POST, instance=editar_casilla)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            editar_casilla = form.save(commit=False)
            # Podemos guardarla cuando queramos
            editar_casilla.save()
            return redirect('/eleccion/casilla/listar')

    # Si llegamos al final renderizamos el formulario
    return render(request, "casilla_edit.html", {'form': form})

def add(request):
    # Creamos un formulario vacío
    form = CasillaForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = CasillaForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            agregar_casilla = form.save(commit=False)
            # Podemos guardarla cuando queramos
            agregar_casilla.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/eleccion/casilla/listar')

    # Si llegamos al final renderizamos el formulario
    return render(request, "casilla_agregar.html", {'form': form})



# listado = Casilla.objects.order_by('ubicacion')
# salida = '<br>'.join([q.ubicacion for q in listado])
# return HttpResponse(salida)
