from django import forms  
from app_usuarios.models import Docente, Estudiante, Representante  

class DocenteForm(forms.ModelForm):  
    class Meta:  
        model = Docente  
        fields = ['nombres', 'apellidos', 'identificacion', 'fecha_nacimiento', 'correo_institucional', 'celular', 'direccion']  
        widgets = {  
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),    
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'correo_institucional': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Complete este campo'}),   
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),   
        } 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fecha_nacimiento:
            self.initial['fecha_nacimiento'] = self.instance.fecha_nacimiento.strftime('%Y-%m-%d')

class EstudianteForm(forms.ModelForm):  
    class Meta:  
        model = Estudiante  
        fields = ['nombres', 'apellidos', 'identificacion', 'fecha_nacimiento', 'correo_institucional']  
        widgets = {  
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),    
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'correo_institucional': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Complete este campo'}),    
        }  
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fecha_nacimiento:
            self.initial['fecha_nacimiento'] = self.instance.fecha_nacimiento.strftime('%Y-%m-%d')

class RepresentanteForm(forms.ModelForm):  
    class Meta:  
        model = Representante  
        fields = ['nombres', 'apellidos', 'identificacion', 'fecha_nacimiento', 'correo_personal', 'celular', 'direccion']  
        widgets = {  
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),    
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'correo_personal': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Complete este campo'}),   
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),   
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Complete este campo'}),  
        }  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fecha_nacimiento:
            self.initial['fecha_nacimiento'] = self.instance.fecha_nacimiento.strftime('%Y-%m-%d')
