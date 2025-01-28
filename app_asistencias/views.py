from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from app_asistencias.models import Asistencia
from app_ofertaacademica.models import Paralelo
from app_matriculas.models import Matricula
from django.http import JsonResponse


def view_home(request):
    #Mostramos paralelos
    #Peticion al Modelo Paralelo de la base Datos
    paralelos = Paralelo.objects.all()
    return render(request, 'app_asistencia/asistencias.html', {'paralelos': paralelos, 'parametro': 7})

def listar_asistencias(request, paralelo_id):
    #Buscamos un paralelo por id
    #Ejemplo: si el paralelo J tiene id=1, paralelo contendrá todo lo de J.
    paralelo = get_object_or_404(Paralelo, id=paralelo_id)
    #Filtramos las asistencias por paralelo, y las ordenamos por el atributo fecha
    asistencias = Asistencia.objects.filter(paralelo=paralelo).order_by('-fecha')
    return render(request, 'app_asistencia/listar_asistencias.html', {
        'parametro': 7,
        'paralelo': paralelo,
        'asistencias': asistencias
    })

def tomar_lista(request, paralelo_id):
    #Buscamos un paralelo por id
    #Ejemplo: si el paralelo J tiene id=1, paralelo contendrá todo lo de J.
    paralelo = get_object_or_404(Paralelo, id=paralelo_id)
    estudiantes = Matricula.objects.filter(paralelo=paralelo)
    
    #Filtramos los estudiantes pertenecientes a una matrícula por paralelo.

    context = {
        'parametro': 7,
        'paralelo': paralelo,
        'estudiantes': estudiantes,
        'fecha': timezone.localtime().date()  # Usa la fecha local
    }
    return render(request, 'app_asistencia/tomar_lista.html', context)


def registrar_asistencias(request, paralelo_id):
    #La petición debe ser POST siempre porque es un CREATE (nuevo_registro)
    if request.method != "POST":
        return redirect('app_asistencias:tomar_lista', paralelo_id=paralelo_id)
        

    #Capturas el paralelo por el id
    paralelo = get_object_or_404(Paralelo, id=paralelo_id)
    #Validamos que solo pueda procesarse la petición del registro de asistencia, 1 por día.
    fecha = request.POST.get('fecha')


    
    # Procesar cada estudiante
    #Recorremos la petición POST
    for key, value in request.POST.items():
        if key.startswith('estudiante_'):
            estudiante_id = key.split('_')[1]
            matricula = get_object_or_404(Matricula, id=estudiante_id, paralelo=paralelo)
            # Ahora manejamos 'presente' o 'ausente' 
            asistio = (value == 'presente')
            
            #Actualizamos a creamos la asistencia
            Asistencia.objects.update_or_create(
                paralelo=paralelo,
                matricula=matricula,
                fecha=fecha,
                defaults={'asistio': asistio}
            )
    
    return redirect('app_asistencias:asistencias_paralelo', paralelo_id=paralelo_id)




def actualizar_asistencia(request, asistencia_id):
    #La asistencia llegar por id en la URL
    if request.method == 'POST':
        asistencia = get_object_or_404(Asistencia, id=asistencia_id)
        #Capturamos la asistencia por ID
        #Actualizamos
        nuevo_estado = request.POST.get('estado') == 'true'
        asistencia.asistio = nuevo_estado
        asistencia.save()
        #Devolvemos un Json para validar desde la plantilla, para no recargar la página
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)