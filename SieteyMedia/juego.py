import json
import random
import os   # 👈 añade este import

# Ruta absoluta al archivo cartas.json, en la misma carpeta que este script
ruta = os.path.join(os.path.dirname(__file__), "cartas.json")

with open(ruta, "r", encoding="utf-8") as f:
    baraja = json.load(f)["cartas"]

# Barajar
random.shuffle(baraja)

puntos = 0.0
print("🎲 Bienvenido al juego de Siete y Media\n")

while puntos < 7.5 and baraja:
    carta = baraja.pop()
    puntos += carta["valor"]

    print(f"Has sacado: {carta['numero']} de {carta['palo']} (valor {carta['valor']})")
    print(f"Total de puntos: {puntos}\n")

    if puntos == 7.5:
        print("🎉 ¡Has ganado con siete y media!")
        break
    elif puntos > 7.5:
        print("💥 Te pasaste de siete y media. Pierdes.")
        break
    else:
        seguir = input("¿Quieres otra carta? (s/n): ").strip().lower()
        while seguir not in ("s", "n"):
            seguir = input("Responde con 's' o 'n': ").strip().lower()
        if seguir == "n":
            print(f"🛑 Te plantas con {puntos} puntos.")
            break

if not baraja and puntos < 7.5:
    print("Se acabaron las cartas. Resultado final:", puntos)
