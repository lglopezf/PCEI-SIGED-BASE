from django.shortcuts import render, redirect
from .models import Grado, Asignatura
from app_configuracion.models import Institucion
from app_grados.models import Nivel, SubNivel
from app_librocalificaciones.models import Librocalificacion

def grados(request):
    grados = Grado.objects.first()
    datos = {'grado': grados, 'parametro': 3}
    return render(request, 'app_grados/inicio.html', datos)

def grados_crear(request):
    if request.method == 'POST':
        grados = Grado()
        grados.nombre = request.POST.get('nombre')
        grados.institucion_id = request.POST.get('institucion')
        grados.nivel_id = request.POST.get('nivel')
        grados.subnivel_id = request.POST.get('subnivel')
        grados.libro_calificacion_id = request.POST.get('librocalificacion')
        grados.save()
        return redirect('app_grados:grados_listar')
    else:
        instituciones = Institucion.objects.all()
        niveles = Nivel.objects.all()
        subniveles = SubNivel.objects.all()
        librocalificaciones = Librocalificacion.objects.all()
        datos = {
            'parametro': 3,
            'instituciones': instituciones,
            'niveles': niveles,
            'subniveles': subniveles,
            'librocalificaciones': librocalificaciones
        }
        return render(request, 'app_grados/grados_crear.html', datos)

def grados_listar(request):
    grados = Grado.objects.all().order_by('nombre')
    datos = {'grado': grados, 'parametro': 3}
    return render(request, 'app_grados/grados_listar.html', datos)

def grados_editar(request, id):
    grados = Grado.objects.get(id=id)

    if request.method == "POST":
        grados.nombre = request.POST.get('nombre')
        grados.institucion_id = request.POST.get('institucion')
        grados.nivel_id = request.POST.get('nivel')
        grados.subnivel_id = request.POST.get('subnivel')
        grados.libro_calificacion_id = request.POST.get('librocalificacion')
        grados.save()
        return redirect('app_grados:grados_listar')
    else:
        instituciones = Institucion.objects.all()
        niveles = Nivel.objects.all()
        subniveles = SubNivel.objects.all()
        librocalificaciones = Librocalificacion.objects.all()
        datos = {
            'parametro': 3,
            'item': grados,
            'instituciones': instituciones,
            'niveles': niveles,
            'subniveles': subniveles,
            'librocalificaciones': librocalificaciones
        }
        return render(request, 'app_grados/grados_crear.html', datos)

def grados_eliminar(request, id):
    grado = Grado.objects.get(id=id)
    grado.delete()
    return redirect('app_grados:grados_listar')

# Asignaturas............................................


def asignaturas_crear(request):
    if request.method == 'POST':
        nombre_asignatura = request.POST.get('nombre')
        grado= Grado.objects.get(id=request.POST.get('grado'))          
        asignatura = Asignatura(nombre=nombre_asignatura, grado=grado)  
        asignatura.save()
        return redirect('app_grados:asignaturas_listar')  
    else:
        grados = Grado.objects.all()
        datos = {'grados': grados, 'parametro': 3}
        return render(request, 'app_grados/asignaturas_crear.html', datos) 
    
def asignaturas_editar(request, id):
    asignatura = Asignatura.objects.get(id=id)
    if request.method == 'POST':
        asignatura.nombre = request.POST.get('nombre')
        grado = Grado.objects.get(id=request.POST.get('grado'))
        
        asignatura.grado = grado
        asignatura.save()
        return redirect('app_grados:asignaturas_listar')
    else:
        grados = Grado.objects.all()
        datos = {'item': asignatura, 'grados': grados, 'parametro': 3}
        return render(request, 'app_grados/asignaturas_crear.html', datos)
    

def asignaturas_listar(request):
    asignaturas = Asignatura.objects.all()
    datos = {'asignaturas': asignaturas, 'parametro': 3}
    return render(request, 'app_grados/asignaturas_listar.html', datos)

def asignaturas_eliminar(request, id): 
    asignaturas = Asignatura.objects.get(id=id)
    asignaturas.delete()  
    return redirect('app_grados:asignaturas_listar')


