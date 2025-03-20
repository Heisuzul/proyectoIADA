from itertools import product
from utils import leer_archivo_entrada,calcular_conflicto_interno,calcular_esfuerzo
import math

ruta_archivo = "../../data/entrada.txt"
red_social, R_max = leer_archivo_entrada(ruta_archivo)

def modciFB(red_social):
    todas_estrategias = product(*[range(n_i + 1) for n_i, _, _, _ in red_social])
    
    mejor_estrategia = None
    mejor_conflicto = float('inf')
    mejor_esfuerzo = 0
    
    for estrategia in todas_estrategias:
        esfuerzo = calcular_esfuerzo(red_social, estrategia)
        if esfuerzo <= R_max:  
            conflicto = calcular_conflicto_interno(red_social, estrategia)
            if conflicto < mejor_conflicto:
                mejor_conflicto = conflicto
                mejor_estrategia = estrategia
                mejor_esfuerzo = esfuerzo
    
    return mejor_estrategia, mejor_esfuerzo, mejor_conflicto


mejor_estrategia, mejor_esfuerzo, mejor_conflicto = modciFB(red_social)
print("Conflicto Interno: ", calcular_conflicto_interno(red_social, (1,0,0)))
print("Esfuerzo: ", calcular_esfuerzo(red_social, (1,0,0)))
print("Mejor estrategia:", mejor_estrategia)
print("Esfuerzo requerido:", mejor_esfuerzo)
print("Conflicto interno resultante:", mejor_conflicto)


