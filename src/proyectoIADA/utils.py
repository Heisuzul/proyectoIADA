import sys
import math

ruta_archivo = "../../data/entrada.txt"

def leer_archivo_entrada(ruta_archivo):
    """
    Lee un archivo de entrada y extrae los datos de la red social y el valor máximo de esfuerzo.
    
    :param ruta_archivo: Ruta del archivo de entrada.
    :return: Una tupla (red_social, R_max), donde red_social es una lista de tuplas con los datos de cada grupo de agentes,
             y R_max es el valor máximo de esfuerzo permitido.
    """
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    n = int(lineas[0].strip())
    red_social = []
    for i in range(1, n + 1):
        datos = list(map(float, lineas[i].strip().split(',')))
        red_social.append((int(datos[0]), int(datos[1]), int(datos[2]), datos[3]))
    
    R_max = int(lineas[n + 1].strip())
    return red_social, R_max


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


red_social = leer_archivo_entrada(ruta_archivo)
print("Red social cargada:", red_social)
