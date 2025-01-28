from django.shortcuts import render, redirect
from django.urls import reverse
from app_ofertaacademica.models import Aniolectivo, Distributivo
from app_librocalificaciones.models import Periodoacademico, Actividad
from .models import Actividad, Calificacionevaluacion,Calificacionactividad, Calificacionperiodo, Calificacionfinal


def calificaciones(request):
    anio_lectivos = Aniolectivo.objects.all()
    datos = {'parametro': 8, 'anio_lectivos': anio_lectivos}
    return render(request, 'app_calificaciones/inicio.html', datos)


def verlibro(request,id):
    distributivo = Distributivo.objects.filter(id=id).first()
    matriculas= distributivo.get_matriculas()
    libro_calificaciones=distributivo.asignatura.grado.libro_calificacion
    datos = {'parametro': 8, 'distributivo': distributivo, 'libro_calificaciones': libro_calificaciones,'matriculas':matriculas}
    return render(request, 'app_calificaciones/verlibro.html', datos)


def verevaluaciones(request,iddistributivo, idperiodoacademico):
    distributivo = Distributivo.objects.filter(id=iddistributivo).first()
    matriculas= distributivo.get_matriculas()
    periodoacademico = Periodoacademico.objects.filter(id=idperiodoacademico).first()
    datos = {'parametro': 8, 'distributivo': distributivo, 'periodoacademico': periodoacademico,'matriculas':matriculas}
    return render(request, 'app_calificaciones/verevaluaciones.html', datos)


def ingresarnotas(request, iddistributivo, idactividades):
    distributivo = Distributivo.objects.filter(id=iddistributivo).first()
    matriculas= distributivo.get_matriculas()
    actividad = Actividad.objects.filter(id=idactividades).first()
    librocalificacion = distributivo.paralelo.grado.libro_calificacion
    periodoacademico = actividad.evaluacion.periodo_academico
    datos = {'parametro': 8, 'distributivo': distributivo, 'actividad': actividad,'matriculas':matriculas, 'periodoacademico': periodoacademico}
    return render(request, 'app_calificaciones/ingresarnotas.html', datos)


def guardarnotas(request, iddistributivo, idactividades):
    distributivo = Distributivo.objects.filter(id=iddistributivo).first()
    matriculas= distributivo.get_matriculas()
    actividad = Actividad.objects.filter(id=idactividades).first()
    print(request.POST)

    for matricula in matriculas:
        nota=request.POST.get(str(matricula.id))

        matricula.generar_calificacion_final(distributivo)
        matricula.guardar_nota(actividad, nota)

        print(matricula.id, nota)
    return redirect(reverse('app_calificaciones:verevaluaciones', args=[distributivo.id, actividad.evaluacion.periodo_academico.id]))


def calcularpromedio_calificacionfinal(request, iddistributivo):
    distributivo = Distributivo.objects.filter(id=iddistributivo).first()
    matriculas= distributivo.get_matriculas()

    for matricula in matriculas:

        calificacionfinal = Calificacionfinal.objects.filter(matricula=matricula).first()
        calificaciones_periodos = Calificacionperiodo.objects.filter(calificacion_final=calificacionfinal).all()
        suma_promedio=0
        
        for calificacion_periodo in calificaciones_periodos:
        
          suma_promedio += calificacion_periodo.nota or 0

        
        if calificaciones_periodos.count() > 0:
            promedio=suma_promedio / calificaciones_periodos.count()
        else:
            promedio= 0
        if calificacionfinal:
            calificacionfinal.nota = promedio
            calificacionfinal.save()   
    return redirect(reverse('app_calificaciones:verlibro', args=[distributivo.id]))


def calcularpromedios_periodo_evaluaciones(request, iddistributivo, idperiodoacademico):
    distributivo = Distributivo.objects.filter(id=iddistributivo).first()
    matriculas= distributivo.get_matriculas()
    periodoacademico = Periodoacademico.objects.filter(id=idperiodoacademico).first()

    for matricula in matriculas:
        suma_promedio = 0
        calificacion_periodo=Calificacionperiodo.objects.filter(calificacion_final__matricula=matricula,
                                                                periodo_academico = periodoacademico).first()

        calificacionevaluaciones= Calificacionevaluacion.objects.filter(calificacion_periodo=calificacion_periodo)

        for calificacionevaluacion in calificacionevaluaciones: 
            calificacionactividades= Calificacionactividad.objects.filter(calificacion_evaluacion=calificacionevaluacion)

            suma_notas=0
            total_actividades=0

            for calificacionactividad in calificacionactividades:
                suma_notas +=calificacionactividad.nota
                total_actividades += 1

            if total_actividades > 0:
                promedio = suma_notas / total_actividades
            else:
                promedio = 0
        
            calificacionevaluacion.nota = promedio
            calificacionevaluacion.save()
            
            #calcular promedio final de periodos

            suma_promedio += promedio

        if calificacionevaluaciones.count() > 0:
            promedio = suma_promedio/calificacionevaluaciones.count()
        else:
            promedio=0
        
        calificacion_periodo.nota = promedio
        calificacion_periodo.save()
    return redirect(reverse('app_calificaciones:verevaluaciones', args=[distributivo.id, periodoacademico.id]))
        
