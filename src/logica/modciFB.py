from itertools import product
from src.logica.utils import leer_archivo_entrada,calcular_conflicto_interno,calcular_esfuerzo, modCI

def modciFB(red_social):
    _, R_max = red_social  # Extraemos R_max de la tupla
    
    todas_estrategias = product(*[range(n_i + 1) for n_i, _, _, _ in red_social[0]])
    
    mejor_estrategia = None
    mejor_conflicto = float('inf')
    mejor_esfuerzo = 0
    
    for estrategia in todas_estrategias:
        esfuerzo = calcular_esfuerzo(red_social, estrategia)
        if esfuerzo <= R_max:  # Usa el valor leído desde la tupla red_social
            nueva_red = modCI(red_social, estrategia)  # Aplicamos la estrategia
            conflicto = calcular_conflicto_interno(nueva_red)  # Evaluamos CI después de la modificación
            if conflicto < mejor_conflicto:
                mejor_conflicto = conflicto
                mejor_estrategia = estrategia
                mejor_esfuerzo = esfuerzo
    
    return (mejor_estrategia, mejor_esfuerzo, mejor_conflicto)

