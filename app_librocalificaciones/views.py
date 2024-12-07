from django.shortcuts import render


def libro_calificaciones(request):
    datos = {'parametro': 5}
    return render(request, 'app_librocalificaciones/inicio.html', datos)