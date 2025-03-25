import math

ruta_archivo = "../../data/entrada.txt"

def leer_archivo_entrada(ruta_archivo):
    """
    Lee un archivo de entrada y extrae los datos de la red social y el valor máximo de esfuerzo.
    
    :param ruta_archivo: Ruta del archivo de entrada.
    :return: Una tupla red_social, donde el primer elemento es la secuencia de agentes y el segundo es R_max.
    """
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    n = int(lineas[0].strip())
    secuencia_agentes = []
    for i in range(1, n + 1):
        datos = list(map(float, lineas[i].strip().split(',')))
        secuencia_agentes.append((int(datos[0]), int(datos[1]), int(datos[2]), datos[3]))
    
    R_max = int(lineas[n + 1].strip())
    
    red_social = (secuencia_agentes, R_max)
    print("Red social cargada:", red_social)

    return (secuencia_agentes, R_max)


def calcular_conflicto_interno(red_social):
    numerador = 0
    denominador = 0
    
    for n_i, op1, op2, _ in red_social[0]:
        numerador += n_i * (op1 - op2) ** 2
        denominador += n_i
    
    return numerador / denominador if denominador > 0 else 0

def calcular_esfuerzo(red_social, estrategia):
    esfuerzo = 0
    for i, (n_i, op1, op2, rigidez) in enumerate(red_social[0]):
        esfuerzo += math.ceil(abs(op1 - op2) * rigidez * estrategia[i])
    return esfuerzo

def modCI(red_social, estrategia):
    secuencia_agentes, R_max = red_social
    nueva_secuencia = []
    
    for i, (n_i, op1, op2, rigidez) in enumerate(secuencia_agentes):
        if estrategia[i] < n_i:  # Solo agregamos agentes restantes
            nueva_secuencia.append((n_i - estrategia[i], op1, op2, rigidez))
    
    return (nueva_secuencia, R_max)


