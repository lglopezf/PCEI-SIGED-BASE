from django.shortcuts import render


def grados(request):
    datos = {'parametro': 3}
    return render(request, 'app_grados/inicio.html', datos)