from itertools import product
from src.logica.utils import calcular_conflicto_interno,calcular_esfuerzo, aplicar_estrategia

def modciFB(red_social):
    _, secuencia_agentes, R_max = red_social  

    mejor_estrategia = None
    mejor_conflicto = float('inf')
    mejor_esfuerzo = 0

    todas_estrategias = product(*[range(n_i + 1) for n_i, _, _, _ in secuencia_agentes])
    
    for estrategia in todas_estrategias:
        esfuerzo = calcular_esfuerzo(red_social, estrategia)

        if esfuerzo <= R_max:  # Respetamos la restricción de esfuerzo
            nueva_red = aplicar_estrategia(red_social, estrategia)  # Aplicamos la estrategia
            conflicto = calcular_conflicto_interno(nueva_red)  # Evaluamos CI con el denominador fijo

            if conflicto < mejor_conflicto:
                mejor_conflicto = conflicto
                mejor_estrategia = estrategia
                mejor_esfuerzo = esfuerzo
    
    return (mejor_estrategia, mejor_esfuerzo, mejor_conflicto)

