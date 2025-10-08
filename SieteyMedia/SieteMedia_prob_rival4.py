from itertools import combinations


#  Siete y Media

PALOS = ["oros", "copas", "espadas", "bastos"]
NUMS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
MAZO = [(p, n) for p in PALOS for n in NUMS]

def valor_carta(n):
    """Devuelve el valor de una carta en Siete y media."""
    return 0.5 if n in (10, 11, 12) else n

def puntos_mano(mano):
    """Suma los valores de una mano."""
    return sum(valor_carta(num) for _, num in mano)

def resultado(p_hero, p_rival):
    """Devuelve 1 si gana el héroe, -1 si pierde, 0 si empata."""
    if p_hero > 7.5 and p_rival > 7.5:
        return 0
    if p_hero > 7.5:
        return -1
    if p_rival > 7.5:
        return 1
    if p_hero > p_rival:
        return 1
    if p_hero < p_rival:
        return -1
    return 0

def simular_probabilidad(hero_known, rival_known, hero_total, rival_total):
    """Simula todas las combinaciones posibles exactas."""
    usadas = set(hero_known + rival_known)
    mazo_rest = [c for c in MAZO if c not in usadas]
    faltan_hero = hero_total - len(hero_known)
    faltan_rival = rival_total - len(rival_known)

    casos_posibles = 0
    casos_favorables = 0

    for cartas_rival in combinations(mazo_rest, faltan_rival):
        mazo_despues_rival = [c for c in mazo_rest if c not in cartas_rival]
        p_rival = puntos_mano(rival_known + list(cartas_rival))

        for cartas_hero in combinations(mazo_despues_rival, faltan_hero):
            casos_posibles += 1
            p_hero = puntos_mano(hero_known + list(cartas_hero))
            if resultado(p_hero, p_rival) == 1:
                casos_favorables += 1

    if casos_posibles == 0:
        return 0, 0, 0.0, 0.0
    ganar_pct = round(casos_favorables / casos_posibles * 100, 1)
    perder_pct = round(100 - ganar_pct, 1)
    return casos_posibles, casos_favorables, ganar_pct, perder_pct

# Mi carta y carta rival
hero_known = [("oros", 6)]      # carta conocida del héroe
rival_known = [("bastos", 2)]   # carta visible del rival


# Mostrar resultados

print("=== Probabilidades en Siete y Media (1–4 cartas jugador y rival) ===")
print(" Heroe | Rival | Casos posibles | Favorables | Ganar % | Perder %")
print("-------+--------+----------------+-------------+---------+---------")

total_global = 0

for hero_total in range(1, 5):      # héroe con 1 a 4 cartas
    for rival_total in range(1, 5): # rival con 1 a 4 cartas
        cp, cf, pg, pp = simular_probabilidad(hero_known, rival_known, hero_total, rival_total)
        total_global += cp
        print(f"  {hero_total:<5}| {rival_total:<6}| {cp:<15}| {cf:<11}| {pg:<7}| {pp:<7}")

print("\nTotal de combinaciones evaluadas:", total_global)
