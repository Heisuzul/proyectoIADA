from itertools import product
from utils import leer_archivo_entrada,calcular_conflicto_interno,calcular_esfuerzo, modCI
import math


def modciFB(red_social):
    _, R_max = red_social  # Extraemos R_max de la tupla
    
    todas_estrategias = product(*[range(n_i + 1) for n_i, _, _, _ in red_social[0]])
    
    mejor_estrategia = None
    mejor_conflicto = float('inf')
    mejor_esfuerzo = 0
    
    for estrategia in todas_estrategias:
        esfuerzo = calcular_esfuerzo(red_social, estrategia)
        if esfuerzo <= R_max:  # Usa el valor leído desde la tupla red_social
            conflicto = calcular_conflicto_interno(red_social, estrategia)
            if conflicto < mejor_conflicto:
                mejor_conflicto = conflicto
                mejor_estrategia = estrategia
                mejor_esfuerzo = esfuerzo
    
    return (mejor_estrategia, mejor_esfuerzo, mejor_conflicto)


# Ejemplo de uso:
ruta_archivo = "../../data/entrada.txt"
red_social = leer_archivo_entrada(ruta_archivo)


mejor_estrategia, mejor_esfuerzo, mejor_conflicto = modciFB(red_social)
nueva_red_social = modCI(red_social, mejor_estrategia)
print("Mejor estrategia:", mejor_estrategia)
print("Esfuerzo requerido:", mejor_esfuerzo)
print("Conflicto interno resultante:", mejor_conflicto)
print("Nueva red social:", nueva_red_social)


