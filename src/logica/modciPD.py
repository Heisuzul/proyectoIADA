import math
from src.logica.utils import calcular_conflicto_interno, aplicar_estrategia

def modciPD(red_social):
    num_grupos, grupos, R_max = red_social

    # dp[i][r] =  mínimo alcanzable usando hasta el grupo i con r de esfuerzo
    dp = [{} for _ in range(num_grupos + 1)]
    dp[0][0] = ([], 0)  # estrategia, conflicto

    for i in range(num_grupos):
        n_i, op1, op2, rigidez = grupos[i]
        delta = abs(op1 - op2)
        contribucion_total = n_i * (op1 - op2) ** 2

        for r_prev in dp[i]:
            estrategia_prev, _ = dp[i][r_prev]

            # Probar con diferentes cantidades de agentes moderados
            for m in range(n_i + 1):  # m: cantidad de agentes a moderar en este grupo
                costo = math.ceil(delta * rigidez * m)
                nuevo_r = r_prev + costo

                if nuevo_r > R_max:
                    continue

                nueva_estrategia = estrategia_prev + [m]
                # Aplicar la estrategia parcial para obtener el nuevo conflicto
                nueva_red = aplicar_estrategia((num_grupos, grupos, R_max), nueva_estrategia + [0] * (num_grupos - len(nueva_estrategia)))
                nuevo_ci = calcular_conflicto_interno(nueva_red)

                if nuevo_r not in dp[i + 1] or nuevo_ci < dp[i + 1][nuevo_r][1]:
                    dp[i + 1][nuevo_r] = (nueva_estrategia, nuevo_ci)

    # Buscar el mejor resultado al final
    mejor_conflicto = float('inf')
    mejor_estrategia = []
    mejor_esfuerzo = 0

    for r, (estrategia, ci) in dp[num_grupos].items():
        if ci < mejor_conflicto:
            mejor_conflicto = ci
            mejor_estrategia = estrategia
            mejor_esfuerzo = r

    return (tuple(mejor_estrategia), mejor_esfuerzo, mejor_conflicto)