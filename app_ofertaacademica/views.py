from django.shortcuts import render


def oferta_academica(request):
    datos = {'parametro': 4}
    return render(request, 'app_ofertaacademica/inicio.html', datos)