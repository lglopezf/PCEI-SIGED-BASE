from django import template

register = template.Library()

@register.filter
def recuperar_nota_actividad_filtro(matricula, actividad):
    
    return matricula.recuperar_nota_actividad(actividad)

@register.filter
def recuperar_nota_evaluacion_filtro(matricula, evaluacion):
    
    return matricula.recuperar_nota_evaluacion(evaluacion)

@register.filter
def recuperar_nota_periodo_filtro(matricula, periodo):
    
    return matricula.recuperar_nota_periodo(periodo)

@register.filter
def recuperar_nota_calificacionfinal_filtro(matricula):
    
    return matricula.recuperar_nota_calificacionfinal()




