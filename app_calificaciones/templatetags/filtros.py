from django import template

register = template.Library()

@register.simple_tag
def recuperar_nota_actividad_filtro(matricula, distributivo, actividad):
    return matricula.recuperar_nota_actividad(distributivo, actividad)

@register.simple_tag
def recuperar_nota_evaluacion_filtro(matricula, distributivo, evaluacion):
    return matricula.recuperar_nota_evaluacion(distributivo, evaluacion)

@register.simple_tag
def recuperar_nota_periodo_filtro(matricula, distributivo, periodo_academico):
    return matricula.recuperar_nota_periodo(distributivo, periodo_academico)

@register.simple_tag
def recuperar_nota_calificacionfinal_filtro(matricula, distributivo):
    return matricula.recuperar_nota_calificacionfinal(distributivo)






