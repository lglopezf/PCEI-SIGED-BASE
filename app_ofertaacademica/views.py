from django.shortcuts import render, redirect, get_object_or_404
from.models import Aniolectivo, Paralelo , Distributivo
from .forms import AniolectivoForm, ParaleloForm, DistributivoForm

def oferta_academica(request):
    datos = {'parametro': 4}
    return render(request, 'app_ofertaacademica/inicio.html', datos)

# oferta_academica  
def admin_aniolectivo(request):  
    aniolectivo = Aniolectivo.objects.all()  
    return render(request, 'app_ofertaacademica/admin_aniolectivo.html', {'parametro': 4, 'aniolectivo': aniolectivo})  

def create_aniolectivo(request):  
    if request.method == "POST":  
        form = AniolectivoForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('app_ofertaacademica:admin_aniolectivo')  
    else:  
        form = AniolectivoForm()  
    return render(request, 'app_ofertaacademica/create_aniolectivo.html', {'parametro': 4, 'form': form})  

def update_aniolectivo(request, pk):  
    aniolectivo = get_object_or_404(Aniolectivo, pk=pk)  
    if request.method == "POST":  
        form = AniolectivoForm(request.POST, instance=aniolectivo)  
        if form.is_valid():  
            form.save()  
            return redirect('app_ofertaacademica:admin_aniolectivo')  
    else:  
        form = AniolectivoForm(instance=aniolectivo)  
    return render(request, 'app_ofertaacademica/update_aniolectivo.html', {'parametro': 4, 'form': form, 'aniolectivo': aniolectivo})  

def delete_aniolectivo(request, pk):  
    aniolectivo = get_object_or_404(Aniolectivo, pk=pk)  
    if request.method == "POST":  
        aniolectivo.delete()  
        return redirect('app_ofertaacademica:admin_aniolectivo')  
    return render(request, 'app_ofertaacademica/delete_aniolectivo.html', {'parametro': 4, 'aniolectivo': aniolectivo}) 

# Paralelos  
def admin_paralelo(request):  
    paralelo = Paralelo.objects.all()  
    return render(request, 'app_ofertaacademica/admin_paralelo.html', {'parametro': 4, 'paralelo': paralelo})  

def create_paralelo(request):  
    if request.method == "POST":  
        form = ParaleloForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('app_ofertaacademica:admin_paralelo')  # Redirige a la lista de paralelo  
    else:  
        form = ParaleloForm()  
    return render(request, 'app_ofertaacademica/create_paralelo.html', {'parametro': 4, 'form': form})  

def update_paralelo(request, pk):  
    paralelo = get_object_or_404(Paralelo, pk=pk)  
    if request.method == "POST":  
        form = ParaleloForm(request.POST, instance=paralelo)  
        if form.is_valid():  
            form.save()  
            return redirect('app_ofertaacademica:admin_paralelo')  # Redirige a la lista de paralelo  
    else:  
        form = ParaleloForm(instance=paralelo)  
    return render(request, 'app_ofertaacademica/update_paralelo.html', {'parametro': 4, 'form': form, 'paralelo': paralelo})  

def delete_paralelo(request, pk):  
    paralelo = get_object_or_404(Paralelo, pk=pk)  
    if request.method == "POST":  
        paralelo.delete()  
        return redirect('app_ofertaacademica:admin_paralelo')  # Redirige a la lista de paralelo  
    return render(request, 'app_ofertaacademica/delete_paralelo.html', {'parametro': 4, 'paralelo': paralelo})





    #Distributivos

def admin_distributivo(request):
    distributivo = Distributivo.objects.all()
    return render(request, 'app_ofertaacademica/admin_distributivo.html',{'parametro': 4, 'distributivo':distributivo})

def create_distributivo(request):
    if request.method == "POST":
        form = DistributivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_ofertaacademica:admin_distributivo')
    else:
        form = DistributivoForm()
    return render(request, 'app_ofertaacademica/create_distributivo.html', {'parametro': 4, 'form': form})


def update_distributivo(request,pk):
    distributivo = get_object_or_404(Distributivo, pk=pk)
    if request.method == "POST":
        form = DistributivoForm(request.POST, instance=distributivo)
        if form.is_valid():
            form.save()
            return redirect('app_ofertaacademica:admin_distributivo')
    else:
        form = DistributivoForm(instance=distributivo)
    return render(request, 'app_ofertaacademica/update_distributivo.html', {'parametro': 4, 'form':form,'distributivo':distributivo})

def delete_distributivo(request,pk):
    distributivo = get_object_or_404(Distributivo, pk=pk)
    if request.method =="POST":
        distributivo.delete()
        return redirect('app_ofertaacademica:admin_distributivo')
    return render(request, 'app_ofertaacademica/delete_distributivo.html', {'parametro': 4, 'distributivo': distributivo})



    