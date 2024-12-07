from django.shortcuts import render


def usuarios(request):
    datos = {'parametro': 2}
    return render(request, 'app_usuarios/inicio.html', datos)