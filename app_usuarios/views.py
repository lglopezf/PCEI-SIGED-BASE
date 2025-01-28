from django.shortcuts import render, redirect, get_object_or_404  
from .models import Docente, Estudiante, Representante
from .forms import DocenteForm, EstudianteForm, RepresentanteForm  


def usuarios(request):
    datos = {'parametro': 2}
    return render(request, 'app_usuarios/inicio.html', datos)

# Docentes  
def admin_docentes(request): 
    docentes = Docente.objects.all()   
    return render(request, 'app_usuarios/admin_docentes.html', {'parametro': 2, 'docentes': docentes})  

def create_docente(request):  
    if request.method == "POST":  
        form = DocenteForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('app_usuarios:admin_docentes')  
    else:  
        form = DocenteForm()  
    return render(request, 'app_usuarios/create_docente.html', {'parametro': 2, 'form': form})  

def update_docente(request, pk):  
    docente = get_object_or_404(Docente, pk=pk)  
    if request.method == "POST":  
        form = DocenteForm(request.POST, instance=docente)  
        if form.is_valid():  
            form.save()  
            return redirect('app_usuarios:admin_docentes')  
    else:  
        form = DocenteForm(instance=docente)  
    return render(request, 'app_usuarios/update_docente.html', {'parametro': 2,'form': form, 'docente': docente})  

def delete_docente(request, pk):  
    docente = get_object_or_404(Docente, pk=pk)  
    if request.method == "POST":  
        docente.delete()  
        return redirect('app_usuarios:admin_docentes')  
    return render(request, 'app_usuarios/delete_docente.html', {'parametro': 2, 'docente': docente})  

# Estudiantes
def admin_estudiantes(request):  
    estudiantes = Estudiante.objects.all()  
    return render(request, 'app_usuarios/admin_estudiante.html', {'parametro': 2, 'estudiantes': estudiantes})  

def create_estudiante(request):  
    if request.method == "POST":  
        form = EstudianteForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('app_usuarios:admin_estudiantes')  
    else:  
        form = EstudianteForm()  
    return render(request, 'app_usuarios/create_estudiante.html', {'parametro': 2, 'form': form})  

def update_estudiante(request, pk):  
    estudiante = get_object_or_404(Estudiante, pk=pk)  
    if request.method == "POST":  
        form = EstudianteForm(request.POST, instance=estudiante)  
        if form.is_valid():  
            form.save()  
            return redirect('app_usuarios:admin_estudiantes')  
    else:  
        form = EstudianteForm(instance=estudiante)  
    return render(request, 'app_usuarios/update_estudiante.html', {'parametro': 2, 'form': form, 'estudiante': estudiante})  

def delete_estudiante(request, pk):  
    estudiante = get_object_or_404(Estudiante, pk=pk)  
    if request.method == "POST":  
        estudiante.delete()  
        return redirect('app_usuarios:admin_estudiantes')  
    return render(request, 'app_usuarios/delete_estudiante.html', {'parametro': 2, 'estudiante': estudiante})  

# Representantes 
def admin_representantes(request):  
    representantes = Representante.objects.all()  
    return render(request, 'app_usuarios/admin_representantes.html', {'parametro': 2, 'representantes': representantes})  

def create_representante(request):  
    if request.method == "POST":  
        form = RepresentanteForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('app_usuarios:admin_representantes')  
    else:  
        form = RepresentanteForm()  
    return render(request, 'app_usuarios/create_representante.html', {'parametro': 2, 'form': form})  

def update_representante(request, pk):  
    representante = get_object_or_404(Representante, pk=pk)  
    if request.method == "POST":  
        form = RepresentanteForm(request.POST, instance=representante)  
        if form.is_valid():  
            form.save()  
            return redirect('app_usuarios:admin_representantes')  
    else:  
        form = RepresentanteForm(instance=representante)  
    return render(request, 'app_usuarios/update_representante.html', {'parametro': 2, 'form': form, 'representante': representante})  

def delete_representante(request, pk):  
    representante = get_object_or_404(Representante, pk=pk)  
    if request.method == "POST":  
        representante.delete()  
        return redirect('app_usuarios:admin_representantes')  
    return render(request, 'app_usuarios/delete_representante.html', {'parametro': 2, 'representante': representante})  