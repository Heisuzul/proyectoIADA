from utils import calcular_conflicto_interno, calcular_esfuerzo, aplicar_estrategia

def modciV(red_social):
    num_grupos, SAG, R_max = red_social
    estrategia = [0] * len(SAG)  # Inicializamos la estrategia
    esfuerzo_usado = 0

    # Calcular la contribución al conflicto y costo por agente
    grupos = []
    for i, (num_agentes, op1, op2, rigidez) in enumerate(SAG):
        if num_agentes == 0 or op1 == op2:
            continue
        contribucion = num_agentes * (op1 - op2) ** 2
        costo_por_agente = abs(op1 - op2) * rigidez
        if costo_por_agente > 0:
            eficiencia = contribucion / costo_por_agente
            grupos.append((i, eficiencia, costo_por_agente, num_agentes))

    # Ordenar por mayor eficiencia (beneficio por unidad de esfuerzo)
    grupos.sort(key=lambda x: x[1], reverse=True)

    # Aplicar estrategia voraz
    for i, _, costo_unitario, disponibles in grupos:
        if esfuerzo_usado >= R_max:
            break
        max_cambiables = min(disponibles, int((R_max - esfuerzo_usado) // costo_unitario))
        if max_cambiables > 0:
            estrategia[i] = max_cambiables
            esfuerzo_usado += max_cambiables * costo_unitario

    # Aplicar estrategia a la red y calcular el nuevo conflicto
    red_moderada = aplicar_estrategia(red_social, estrategia)
    nuevo_conflicto = calcular_conflicto_interno(red_moderada)

    return estrategia, round(esfuerzo_usado), nuevo_conflicto


