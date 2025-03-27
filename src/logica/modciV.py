from utils import calcular_conflicto_interno, calcular_esfuerzo, modCI

def modciV(red_social):
    SAG, R_max = red_social
    n = len(SAG)  # Número de grupos de agentes
    estrategia = [0] * n  # Lista para almacenar cambios por grupo
    esfuerzo_usado = 0

    # 1. Calcular contribución al conflicto y costo por agente
    grupos = []
    for i, (num_agentes, op1, op2, rigidez) in enumerate(SAG):
        contribucion = num_agentes * (op1 - op2) ** 2
        costo_por_agente = abs(op1 - op2) * rigidez
        if costo_por_agente > 0:
            grupos.append((i, contribucion, costo_por_agente, num_agentes))

    # 2. Ordenar por eficiencia (reducción de conflicto por unidad de esfuerzo)
    grupos.sort(key=lambda x: x[1] / x[2], reverse=True)

    # 3. Aplicar estrategia voraz hasta agotar R_max
    for i, contribucion, costo, num_agentes in grupos:
        if esfuerzo_usado >= R_max:
            break
        
        max_cambiables = min(num_agentes, (R_max - esfuerzo_usado) // costo)
        esfuerzo_usado += max_cambiables * costo
        estrategia[i] = max_cambiables

    # 4. Actualizar red social y calcular nuevo conflicto
    nueva_red_social = modCI(red_social, estrategia)
    nuevo_conflicto = calcular_conflicto_interno(nueva_red_social)

    return estrategia, esfuerzo_usado, nuevo_conflicto
