# Ejercicios de probabilidad 

# Función valor_carta 
def valor_carta(carta):
    numero = int(carta[:-1])
    if numero <= 7:
        return numero
    else:
        return 0.5

# 1. Probabilidad de sacar un 5 en la baraja de 40 cartas
casos_favorables = 4   # 4 cincos
casos_posibles = 40
prob_5 = casos_favorables / casos_posibles
print("Probabilidad de sacar un 5:", prob_5)

# 2. Probabilidad de sacar una figura (10, 11 o 12)
casos_favorables = 12  # 3 figuras x 4 palos
prob_figura = casos_favorables / 40
print("Probabilidad de sacar una figura:", prob_figura)

# 3. Probabilidad de pasarse con la próxima carta
def probabilidad_bust(mano):
    # Construir baraja española de 40
    baraja = [f"{r}{s}" for r in [1,2,3,4,5,6,7,10,11,12] for s in ["O","C","E","B"]]
    # Quitar cartas de la mano
    for c in mano:
        baraja.remove(c)
    # Valor actual de la mano
    valor_actual = sum(valor_carta(c) for c in mano)
    limite = 7.5 - valor_actual
    # Contar cartas que hacen bust
    cartas_bust = [c for c in baraja if valor_carta(c) > limite]
    return len(cartas_bust) / len(baraja)

print("Probabilidad de pasarse con mano [5O]:", probabilidad_bust(["5O"]))
print("Probabilidad de pasarse con mano [7O]:", probabilidad_bust(["7O"]))
