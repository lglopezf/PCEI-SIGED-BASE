from django import forms
from app_ofertaacademica.models import Aniolectivo, Paralelo, Distributivo


class AniolectivoForm(forms.ModelForm):  
    class Meta:  
        model = Aniolectivo 
        fields = ['nombre', 'fecha_inicio', 'fecha_fin']  
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),  
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),    
        } 
  
class ParaleloForm(forms.ModelForm):  
    class Meta:  
        model = Paralelo  
        fields = ['nombre', 'grado', 'aniolectivo']   
        widgets = {  
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),  
            'grado': forms.Select(attrs={'class': 'form-control'}),  
            'aniolectivo': forms.Select(attrs={'class': 'form-control'}),  
        }
class DistributivoForm(forms.ModelForm):
    class Meta:
        model = Distributivo
        fields = ['aniolectivo','docente', 'asignatura','paralelo']
        widgets ={
            'aniolectivo': forms.Select(attrs={'class': 'form-control'}),

            'docente': forms.Select(attrs={'class':'form-control'}),
            'asignatura': forms.Select(attrs={'class': 'form-control'}),
            'paralelo':forms.Select(attrs={'class':'form-control'}),
        }