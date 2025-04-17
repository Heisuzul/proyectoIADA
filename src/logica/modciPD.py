import math
from src.logica.utils import calcular_conflicto_interno, aplicar_estrategia

def modciPD(red_social):
    num_grupos, grupos, R_max = red_social

    # dp[i][r] = mínimo alcanzable usando hasta el grupo i con r de esfuerzo
    dp = [{} for _ in range(num_grupos + 1)]
    dp[0][0] = ([], 0)  # estrategia, conflicto

    for i in range(num_grupos):
        n_i, op1, op2, rigidez = grupos[i]
        delta = abs(op1 - op2)
        contribucion_total = n_i * (op1 - op2) ** 2

        for r_prev in dp[i]:
            estrategia_prev, _ = dp[i][r_prev]