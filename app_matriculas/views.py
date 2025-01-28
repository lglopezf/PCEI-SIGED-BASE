from django.shortcuts import render, redirect
from app_ofertaacademica.models import Aniolectivo, Paralelo
from .models import Matricula
from app_usuarios.models import Estudiante

def matriculas(request):
    datos = {'parametro': 6}
    return render(request, 'app_matriculas/inicio.html', datos)

def matriculados_lista(request):
    matriculas = Matricula.objects.all()
    return render(request, 'app_matriculas/matriculados_lista.html', {'parametro': 6, 'matriculas': matriculas})

def matriculas_crear(request):
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        paralelo_id = request.POST.get('paralelo')
        anio_lectivo_id = request.POST.get('aniolectivo')

        estudiante = Estudiante.objects.get(id=estudiante_id)
        paralelo = Paralelo.objects.get(id=paralelo_id)
        anio_lectivo = Aniolectivo.objects.get(id=anio_lectivo_id)

        matricula = Matricula.objects.create(estudiante=estudiante, paralelo=paralelo, aniolectivo=anio_lectivo)
        return redirect('app_matriculas:matriculados_lista')

    estudiantes = Estudiante.objects.all()
    paralelos = Paralelo.objects.all()
    anios_lectivos = Aniolectivo.objects.all()
    return render(request, 'app_matriculas/matriculados_form.html', {
        'parametro': 6,
        'estudiantes': estudiantes,
        'paralelos': paralelos,
        'anios_lectivos': anios_lectivos,
    })

def matriculas_editar(request, id):
    matricula = Matricula.objects.get(id=id)

    if request.method == 'POST':
        
        estudiante_id = request.POST.get('estudiante')
        paralelo_id = request.POST.get('paralelo')
        anio_lectivo_id = request.POST.get('aniolectivo')


        matricula.estudiante = Estudiante.objects.get(id=estudiante_id)
        matricula.paralelo = Paralelo.objects.get(id=paralelo_id)
        matricula.año_lectivo = Aniolectivo.objects.get(id=anio_lectivo_id)
        matricula.save()

        return redirect('app_matriculas:matriculados_lista')

    estudiantes = Estudiante.objects.all()
    paralelos = Paralelo.objects.all()
    anios_lectivos = Aniolectivo.objects.all()
    return render(request, 'app_matriculas/matriculados_form.html', {
        'parametro': 6,
        'estudiantes': estudiantes,
        'paralelos': paralelos,
        'anios_lectivos': anios_lectivos,
        'matricula': matricula,
    })

def matriculas_eliminar(request, id):
    matricula = Matricula.objects.get(id=id)
    matricula.delete()
    return redirect('app_matriculas:matriculados_lista')
