from django.shortcuts import render
from app_ofertaacademica.models import Aniolectivo

def asistencias(request):
    anio_lectivos = Aniolectivo.objects.all()
    datos = {'parametro': 7, 'anio_lectivos': anio_lectivos}
    return render(request, 'app_asistencia/inicio.html', datos)