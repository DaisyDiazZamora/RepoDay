from django.http import HttpResponse
from .models import Funcionario
from django.shortcuts import render
from .forms import FuncionarioForm
from django.shortcuts import redirect

def listar(request):
 lista_funcionario = Funcionario.objects.order_by('nombrecompleto')
 return render(request, 'funcionario_listar.html',context= {'lista_funcionario':lista_funcionario})


#def add(request):
# agregar_casilla = Casilla.objects.order_by('ubicacion')
 #return render(request, 'add.html',context= {'agregar_casilla':agregar_casilla})


def delete(request, funcionario_id):
 eliminar_funcionario = Funcionario.objects.get(id=funcionario_id)
 eliminar_funcionario.delete()
 return redirect('/eleccion/funcionario/listar')



def edit(request, funcionario_id):
    # Recuperamos la instancia de la persona
    editar_funcionario = Funcionario.objects.get(id=funcionario_id)

    # Creamos el formulario con los datos de la instancia
    form = FuncionarioForm(instance=editar_funcionario)

    # Comprobamos si se ha enviado el formulario 
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = FuncionarioForm(request.POST, instance=editar_funcionario)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            editar_funcionario = form.save(commit=False)
            # Podemos guardarla cuando queramos
            editar_funcionario.save()
            return redirect('/eleccion/funcionario/listar')

    # Si llegamos al final renderizamos el formulario
    return render(request, "funcionario_edit.html", {'form': form})

def add(request):
    # Creamos un formulario vacío
    form = FuncionarioForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = FuncionarioForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            agregar_funcionario = form.save(commit=False)
            # Podemos guardarla cuando queramos
            agregar_funcionario.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/eleccion/funcionario/listar')

    # Si llegamos al final renderizamos el formulario
    return render(request, "funcionario_agregar.html", {'form': form})



# listado = Casilla.objects.order_by('ubicacion')
# salida = '<br>'.join([q.ubicacion for q in listado])
# return HttpResponse(salida)
