from django.shortcuts import render, redirect
from app_librocalificaciones.models import Librocalificacion, Evaluacion, Periodoacademico, Actividad
from django.contrib import messages

def inicio(request):
    datos = {'parametro': 5}
    return render(request, 'app_librocalificaciones/inicio.html', datos)

def libro_lista(request):
    libro_calificaciones = Librocalificacion.objects.all()
    datos = {'parametro': 5, 'librocalificaciones': libro_calificaciones}
    return render(request, 'app_librocalificaciones/libro_calificaciones_lista.html', datos)

def libro_crear(request):
    datos = {'parametro': 5}

    if request.method == 'POST':

        nombre = request.POST.get('nombre')

        if Librocalificacion.objects.filter(nombre=nombre).exists():
            messages.warning(request, 'Ya existe un libro de calificación para %s' % nombre)
            return render(request, 'app_librocalificaciones/libro_calificaciones_form.html', datos)

        libro = Librocalificacion ()
        libro.nombre = nombre
        libro.save()
        return redirect('app_librocalificaciones:libro_lista')
    else:
        
        return render(request, 'app_librocalificaciones/libro_calificaciones_form.html', datos)
                        
def libro_editar(request, id):
    libro = Librocalificacion.objects.get(id=id)
    datos = {'parametro': 5, 'librocalificaciones': libro_calificaciones}

    if request.method == 'POST':

        if Librocalificacion.objects.filter(nombre=nombre).exlude(id=libro.id).exists():
            messages.warning(request, 'Ya existe un libro de calificación para %s' % nombre)
            return render(request, 'app_librocalificaciones/libro_calificaciones_form.html', datos)

        libro.nombre = request.POST.get('nombre')
        libro.save()
        return redirect('app_librocalificaciones:libro_lista')
    else:
        
        return render(request, 'app_librocalificaciones/libro_calificaciones_form.html', datos)

def libro_eliminar(request, id):
    libro_calificaciones = Librocalificacion.objects.filter(id=id).first()
    libro_calificaciones.delete()
    return redirect('app_librocalificaciones:libro_lista')
 
def PERIODO_LISTA(request):
    periodo = Periodoacademico.objects.all()
    datos = {'parametro': 5, 'periodo':periodo}
    
    return render (request,'app_librocalificaciones/PERIODO_LISTAR.html', datos )

def PERIODO_CREAR(request): 
    datos = {'parametro': 5}
    if request.method == 'POST':
        periodoacademico = Periodoacademico()
        periodoacademico.nombre = request.POST.get('nombre')
        periodoacademico.orden= request.POST.get('orden')
        periodoacademico.librocalificacion_id= request.POST.get('librocalificacion')
        periodoacademico.save()

        return redirect ('app_librocalificaciones:PERIODO_LISTA')
    else:
        libro_calificaciones= Librocalificacion.objects.all()
        datos['libro_calificaciones']= libro_calificaciones
        return render(request,'app_librocalificaciones/PERIODO_FORM.html', datos )

def PERIODO_EDITAR(request, id): 
    datos = {'parametro': 5}
    periodoacademico = Periodoacademico.objects.filter(id=id).first()
    if request.method == 'POST':
        
        periodoacademico.nombre = request.POST.get('nombre')
        periodoacademico.orden= request.POST.get('orden')
        periodoacademico.librocalificacion_id= request.POST.get('librocalificacion')
        periodoacademico.save()

        return redirect ('app_librocalificaciones:PERIODO_LISTA')
    else:
        libro_calificaciones= Librocalificacion.objects.all()

        datos['libro_calificaciones']= libro_calificaciones
        datos['periodoacademico']= periodoacademico
        
        return render(request,'app_librocalificaciones/PERIODO_FORM.html', datos )

def PERIODO_ELIMINAR(request, id):    
    periodo= Periodoacademico.objects.filter(id=id).first()
    periodo.delete()
    return redirect('app_librocalificaciones:PERIODO_LISTA')


def evaluacion_lista(request):
    evaluaciones = Evaluacion.objects.all()
    datos = {'parametro': 5, 'evaluaciones':evaluaciones}
     
    return render(request, 'app_librocalificaciones/evaluacion_lista.html', datos)

def evaluacion_crear(request):
    datos = {'parametro': 5}
    if request.method == 'POST':

        evaluacion = Evaluacion()
        evaluacion.nombre = request.POST.get('nombre')
        evaluacion.ponderado= request.POST.get('ponderado') if request.POST.get('ponderado') else None
        evaluacion.periodo_academico_id = request.POST.get('periodo_academico')
        evaluacion.save()

        return redirect('app_librocalificaciones:evaluacion_lista')  
    else:
        periodosacademicos=Periodoacademico.objects.all()
        datos = {'parametro': 5, 'periodosacademicos': periodosacademicos}
        return render(request, 'app_librocalificaciones/evaluacion_form.html', datos)

def evaluacion_editar(request, id):
    datos = {'parametro': 5}
    evaluacion = Evaluacion.objects.filter(id=id).first()
    if request.method == 'POST':
        evaluacion = Evaluacion.objects.filter(id=id).first()
        evaluacion.nombre = request.POST.get('nombre')
        evaluacion.ponderado = request.POST.get('ponderado') if request.POST.get('ponderado') else None 
        evaluacion.periodo_academico_id= request.POST.get('periodo_academico')
        evaluacion.save()

        return redirect('app_librocalificaciones:evaluacion_lista')  
     
    else:
        periodosacademicos=Periodoacademico.objects.all()
        datos = {'parametro': 5, 'periodosacademicos': periodosacademicos}
        datos['evaluacion']= evaluacion
        return render(request, 'app_librocalificaciones/evaluacion_form.html', datos)

def evaluacion_eliminar(request, id):    
    evaluacion = Evaluacion.objects.filter(id=id).first()
    evaluacion.delete()
    return redirect('app_librocalificaciones:evaluacion_lista')


def actividad_lista(request,):  
    actividades = Actividad.objects.all()  
    datos = {'parametro': 5, 'actividades':actividades}  
    return render(request, 'app_librocalificaciones/actividad_lista.html', datos)  

def actividad_crear(request):  
    datos = {'parametro': 5}
    if request.method == 'POST':  
        actividad = Actividad()  
        actividad.nombre = request.POST.get('nombre')  
        actividad.tipo = request.POST.get('tipo') 
        actividad.evaluacion_id = request.POST.get('evaluacion') 
        actividad.save() 
        return redirect('app_librocalificaciones:actividad_lista')
    else:
        evaluaciones=Evaluacion.objects.all()
        datos = {'parametro': 5, 'evaluaciones': evaluaciones}
        return render(request,'app_librocalificaciones/actividad_form.html', datos)

def actividad_editar(request, id):
    datos = {'parametro': 5}
    actividad = Actividad.objects.filter(id=id).first()
    if request.method == 'POST':  
        actividad = Actividad.objects.filter(id=id).first()
        actividad.nombre = request.POST.get('nombre')  
        actividad.tipo = request.POST.get('tipo') 
        actividad.evaluacion_id = request.POST.get('evaluacion') 
        actividad.save() 
        return redirect('app_librocalificaciones:actividad_lista')
    else:
        evaluaciones=Evaluacion.objects.all()
        datos = {'parametro': 5, 'evaluaciones': evaluaciones}
        datos['actividad']= actividad
        return render(request,'app_librocalificaciones/actividad_form.html', datos)

def actividad_eliminar(request,id):
        actividad = Actividad.objects.filter(id=id).first()
        actividad.delete()
        return redirect('app_librocalificaciones:actividad_lista')
    