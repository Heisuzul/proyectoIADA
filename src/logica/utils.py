import math

def leer_archivo_entrada(ruta_archivo):
    """
    Lee un archivo de entrada y extrae los datos de la red social, 
    incluyendo el número inicial de grupos y el valor máximo de esfuerzo.

    :param ruta_archivo: Ruta del archivo de entrada.
    :return: Una tupla (secuencia_agentes, R_max, num_grupos).
    """
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    num_grupos = int(lineas[0].strip())  # Se extrae el número de grupos inicial
    secuencia_agentes = []

    for i in range(1, num_grupos + 1):
        datos = list(map(float, lineas[i].strip().split(',')))
        secuencia_agentes.append((int(datos[0]), int(datos[1]), int(datos[2]), datos[3]))

    R_max = int(lineas[num_grupos + 1].strip())  # Última línea es R_max
    
    red_social = (num_grupos,secuencia_agentes, R_max)  # Se incluye en la tupla

    print("Red social cargada:", red_social)  # Debug
    
    return red_social

def calcular_conflicto_interno(red_social):
    num_grupos,secuencia_agentes, R_max = red_social  
    denominador = num_grupos  # Se mantiene fijo

    if num_grupos == 0:
        return 0  # Evitar división por cero

    numerador = sum(n_i * (op1 - op2) ** 2 for n_i, op1, op2, _ in secuencia_agentes)
    
    return numerador / denominador

def calcular_esfuerzo(red_social, estrategia):
    _, secuencia_agentes, _= red_social  # Se ignora R_max y el num_grupos
    return sum(math.ceil(abs(op1 - op2) * rigidez * estrategia[i]) 
               for i, (n_i, op1, op2, rigidez) in enumerate(secuencia_agentes))

def modCI(red_social, estrategia):
    num_grupos, secuencia_agentes, R_max = red_social  # Tomamos el num_grupos inicial

    nueva_secuencia = [(n_i - estrategia[i], op1, op2, rigidez) 
                       for i, (n_i, op1, op2, rigidez) in enumerate(secuencia_agentes) 
                       if estrategia[i] < n_i]  # Filtramos los grupos sin agentes

    return (num_grupos, nueva_secuencia, R_max)  # Mantenemos fijo el denominador inicial




