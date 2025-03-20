from itertools import product
from utils import leer_archivo_entrada
import math

def calcular_conflicto_interno(red_social, estrategia):
    numerador = 0
    denominador = 0
    
    for i, (n_i, op1, op2, rigidez) in enumerate(red_social):
        n_mod = n_i - estrategia[i]  # Número de agentes restantes
        if n_mod > 0:
            numerador += n_mod * (op1 - op2) ** 2
            denominador += n_mod
    
    return numerador / denominador if denominador > 0 else 0

def calcular_esfuerzo(red_social, estrategia):
    esfuerzo = 0
    for i, (n_i, op1, op2, rigidez) in enumerate(red_social):
        esfuerzo += math.ceil(abs(op1 - op2) * rigidez * estrategia[i])
    return esfuerzo

def modciFB(red_social, R_max):
    num_grupos = len(red_social)
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

# Ejemplo de uso:
ruta_archivo = "../../data/entrada.txt"
red_social, R_max = leer_archivo_entrada(ruta_archivo)

mejor_estrategia, mejor_esfuerzo, mejor_conflicto = modciFB(red_social, R_max)
print("Mejor estrategia:", mejor_estrategia)
print("Esfuerzo requerido:", mejor_esfuerzo)
print("Conflicto interno resultante:", mejor_conflicto)
