from django.shortcuts import render
from app_ofertaacademica.models import Aniolectivo

def calificaciones(request):
    anio_lectivos = Aniolectivo.objects.all()
    datos = {'parametro': 8, 'anio_lectivos': anio_lectivos}
    return render(request, 'app_calificaciones/inicio.html', datos)