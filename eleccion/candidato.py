from django.http import HttpResponse
from .models import Candidato
from django.shortcuts import render
from .forms import CandidatoForm
from django.shortcuts import redirect

def listar(request):
 lista_candidato = Candidato.objects.order_by('nombrecompleto')
 return render(request, 'candidato_listar.html',context= {'lista_candidato':lista_candidato})


#def add(request):
# agregar_casilla = Casilla.objects.order_by('ubicacion')
 #return render(request, 'add.html',context= {'agregar_casilla':agregar_casilla})


def delete(request, candidato_id):
 # Recuperamos la instancia de la persona y la borramos
 eliminar_candidato = Candidato.objects.get(id=candidato_id)
 eliminar_candidato.delete()
 # Después redireccionamos de nuevo a la lista
 return redirect('/candidato/listar')


def edit(request, casilla_id):
    # Recuperamos la instancia de la persona
    editar_candidato = Candidato.objects.get(id=candidato_id)

    # Creamos el formulario con los datos de la instancia
    form = CandidatoForm(instance=editar_candidato)

    # Comprobamos si se ha enviado el formulario 
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = CandidatoForm(request.POST, instance=editar_candidato)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            editar_candidato = form.save(commit=False)
            # Podemos guardarla cuando queramos
            editar_candidato.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "candidato_edit.html", {'form': form})

def add(request):
    # Creamos un formulario vacío
    form = CandidatoForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = CandidatoForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            agregar_candidato = form.save(commit=False)
            # Podemos guardarla cuando queramos
            agregar_candidato.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/candidato/listar')

    # Si llegamos al final renderizamos el formulario
    return render(request, "candidato_agregar.html", {'form': form})



# listado = Casilla.objects.order_by('ubicacion')
# salida = '<br>'.join([q.ubicacion for q in listado])
# return HttpResponse(salida)
