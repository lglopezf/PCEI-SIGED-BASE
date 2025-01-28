from django.shortcuts import render, redirect
from app_librocalificaciones.models import Librocalificacion, Evaluacion, Periodoacademico, Actividad


def libro_calificaciones(request):
    datos = {'parametro': 5}
    return render(request, 'app_librocalificaciones/inicio.html', datos)

def inicio(request):
    datos = {'parametro': 5}
    return render(request, 'app_librocalificaciones/inicio.html', datos)

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
#ANA

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
    
#LADY
def lista_libro_calificaciones(request):
    libro_calificaciones = Librocalificacion.objects.all()
    datos = {'parametro': 5, 'librocalificaciones': libro_calificaciones}
    return render(request, 'app_librocalificaciones/lista_libro_calificaciones.html', datos)

def libro_crear(request):
    if request.method == 'POST':
        libro = Librocalificacion ()
        libro.nombre = request.POST.get('nombre')
        libro.save()
        return redirect('app_librocalificaciones:lista_libro_calificaciones')
    else:
        datos = {'parametro': 5, 'librocalificaciones': libro_calificaciones}
        return render(request, 'app_librocalificaciones/libro_form.html', datos)
                        
        
def eliminar_nuevo(request, id):
    libro_calificaciones = Librocalificacion.objects.filter(id=id).first()
    libro_calificaciones.delete()
    return redirect('app_librocalificaciones:lista_libro_calificaciones')
 
        
def editar_nuevo(request, id):
    libro = Librocalificacion.objects.get(id=id)

    if request.method == 'POST':
        libro.nombre = request.POST.get('nombre')
        libro.save()
        return redirect('app_librocalificaciones:lista_libro_calificaciones')
    else:
        datos = {'parametro': 5, 'librocalificaciones': libro_calificaciones}
        return render(request, 'app_librocalificaciones/libro_form.html', datos)

#Leo

def LISTAR_PERIODO(request):
    periodo = Periodoacademico.objects.all()
    datos = {'parametro': 5, 'periodo':periodo}
    
    return render (request,'app_librocalificaciones/LISTAR_PERIODO.html', datos )

def REGISTRAR_PERIODO(request):
    datos = {'parametro': 5}
    periodo = Periodoacademico.objects.all()
    if request.method == 'POST':
        periodo.nombre = request.POST.get()
        periodo.orden = request.POST.get()
        periodo.save()
    return redirect (request, 'app_librocalificaciones:LISTAR_PERIODO', datos )

def CREAR_PERIODO(request): 
    datos = {'parametro': 5}
    if request.method == 'POST':
        periodoacademico = Periodoacademico()
        periodoacademico.nombre = request.POST.get('nombre')
        periodoacademico.orden= request.POST.get('orden')
        periodoacademico.librocalificacion_id= request.POST.get('librocalificacion')
        periodoacademico.save()

        return redirect ('app_librocalificaciones:LISTAR_PERIODO')
    else:
        libro_calificaciones= Librocalificacion.objects.all()
        datos['libro_calificaciones']= libro_calificaciones
        return render(request,'app_librocalificaciones/PERIODO_FORM.html', datos )

def ELIMINAR_PERIODO(request, id):    
    periodo= Periodoacademico.objects.filter(id=id).first()
    periodo.delete()
    return redirect('app_librocalificaciones:LISTAR_PERIODO')

def EDITAR_PERIODO(request, id): 
    datos = {'parametro': 5}
    periodoacademico = Periodoacademico.objects.filter(id=id).first()
    if request.method == 'POST':
        
        periodoacademico.nombre = request.POST.get('nombre')
        periodoacademico.orden= request.POST.get('orden')
        periodoacademico.librocalificacion_id= request.POST.get('librocalificacion')
        periodoacademico.save()

        return redirect ('app_librocalificaciones:LISTAR_PERIODO')
    else:
        libro_calificaciones= Librocalificacion.objects.all()

        datos['libro_calificaciones']= libro_calificaciones
        datos['periodoacademico']= periodoacademico
        
        return render(request,'app_librocalificaciones/PERIODO_FORM.html', datos )


    