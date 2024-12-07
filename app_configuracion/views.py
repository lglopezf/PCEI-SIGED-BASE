from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Institucion

def institucion(request):
    institucion = Institucion.objects.first()
    datos = {'institucion': institucion, 'parametro': 1}
    return render(request, 'app_configuracion/inicio.html', datos)

def institucion_crear(request):

    if request.method == "POST":
        institucion = Institucion()
        institucion.nombre = request.POST.get('nombre')
        institucion.sostenimiento = request.POST.get('sostenimiento')
        institucion.modalidad = request.POST.get('modalidad')
        institucion.save()
        messages.success(request, 'Institución creado exitosamente.')
        return redirect('app_configuracion:institucion')
    else:
        return render(request, 'app_configuracion/configuracion_editar.html', {})

def institucion_editar(request, id):
    institucion = Institucion.objects.get(id=id)

    if request.method == "POST":
        institucion.nombre = request.POST.get('nombre')
        institucion.sostenimiento = request.POST.get('sostenimiento')
        institucion.modalidad = request.POST.get('modalidad')
        institucion.save()
        messages.success(request, 'Institución actualizado exitosamente.')
        return redirect('app_configuracion:institucion')
    else:
        return render(request, 'app_configuracion/configuracion_editar.html', {'institucion': institucion})

def institucion_eliminar(request, id):
    institucion = Institucion.objects.get(id=id)
    institucion.delete()
    messages.success(request, 'Institución eliminado exitosamente.')

    return redirect('app_configuracion:institucion')
