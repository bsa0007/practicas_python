# Probabilidades en Siete y Media

def valor_carta(num):
    """Valor de la carta en siete y media."""
    return 0.5 if num in [10, 11, 12] else num

# Creamos mazo español (40 cartas)
mazo = []
for palo in ["oros", "copas", "espadas", "bastos"]:
    for num in [1,2,3,4,5,6,7,10,11,12]:
        mazo.append((palo, num))

# Cartas ya usadas: rival tiene 5 de bastos, héroe 3 de oros
cartas_usadas = [("bastos", 5), ("oros", 3)]

# Mazo restante
mazo_restante = [c for c in mazo if c not in cartas_usadas]

# Puntos del héroe
puntos_heroe = 3.0

# Contadores
resultados = {
    "plantarse": {"ganar":0, "perder":0},
    "pedir": {"ganar":0, "perder":0}
}

# Simulación de todas las cartas ocultas del rival
total_ocultas = len(mazo_restante)

for oculta in mazo_restante:
    mazo_tmp = [c for c in mazo_restante if c != oculta]
    puntos_oponente = valor_carta(5) + valor_carta(oculta[1])

    # --- Plantarse ---
    if puntos_heroe <= 7.5:
        if puntos_oponente > 7.5 or puntos_heroe > puntos_oponente:
            resultados["plantarse"]["ganar"] += 1
        else:
            resultados["plantarse"]["perder"] += 1

    # --- Pedir carta ---
    for extra in mazo_tmp:
        puntos_heroe2 = puntos_heroe + valor_carta(extra[1])
        if puntos_heroe2 > 7.5:
            resultados["pedir"]["perder"] += 1
        else:
            if puntos_oponente > 7.5 or puntos_heroe2 > puntos_oponente:
                resultados["pedir"]["ganar"] += 1
            else:
                resultados["pedir"]["perder"] += 1

# Totales
total_plantarse = total_ocultas
total_pedir = total_ocultas * (total_ocultas - 1)

# Probabilidades en porcentaje
prob_plantarse = {k: round(v/total_plantarse*100,1) for k,v in resultados["plantarse"].items()}
prob_pedir = {k: round(v/total_pedir*100,1) for k,v in resultados["pedir"].items()}

# Mostrar resultados
print("=== Probabilidades ===")
print(f"Si te plantas: Ganar {prob_plantarse['ganar']}% | Perder {prob_plantarse['perder']}%")
print(f"Si pides carta: Ganar {prob_pedir['ganar']}% | Perder {prob_pedir['perder']}%")
