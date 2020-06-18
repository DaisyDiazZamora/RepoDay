from django.http import HttpResponse
from .models import Rol
from django.shortcuts import render
from .forms import RolForm
from django.shortcuts import redirect

def listar(request):
 lista_rol = Rol.objects.order_by('id')
 return render(request, 'rol_listar.html',context= {'lista_rol':lista_rol})


def delete(request, rol_id):
 eliminar_rol = Rol.objects.get(id=rol_id)
 eliminar_rol.delete()
 return redirect('/eleccion/rol/listar')



def edit(request, rol_id):
    # Recuperamos la instancia de la persona
    editar_rol = Rol.objects.get(id=rol_id)

    # Creamos el formulario con los datos de la instancia
    form = RolForm(instance=editar_rol)

    # Comprobamos si se ha enviado el formulario 
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = RolForm(request.POST, instance=editar_rol)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            editar_rol = form.save(commit=False)
            # Podemos guardarla cuando queramos
            editar_rol.save()
            return redirect('/eleccion/rol/listar')

    # Si llegamos al final renderizamos el formulario
    return render(request, "rol_edit.html", {'form': form})

def add(request):
    # Creamos un formulario vacío
    form = RolForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = RolForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            agregar_rol = form.save(commit=False)
            # Podemos guardarla cuando queramos
            agregar_rol.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/eleccion/rol/listar')

    # Si llegamos al final renderizamos el formulario
    return render(request, "rol_agregar.html", {'form': form})



# listado = Casilla.objects.order_by('ubicacion')
# salida = '<br>'.join([q.ubicacion for q in listado])
# return HttpResponse(salida)
