from django.shortcuts import render


def matriculas(request):
    datos = {'parametro': 6}
    return render(request, 'app_matriculas/inicio.html', datos)