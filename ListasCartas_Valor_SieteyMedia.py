# Ejercicios de listas y funciones

# 1. Crear una lista con algunas cartas de la baraja española
cartas = ["1O", "2O", "5C", "7E", "10B", "12O"]
print("Cartas en la lista:", cartas)

# 2. Mostrar el número de cartas
print("Número de cartas:", len(cartas))

# 3. Acceder a la primera y última carta
print("Primera carta:", cartas[0])
print("Última carta:", cartas[-1])

# 4. Función para calcular el valor de una carta en Siete y Media
def valor_carta(carta):
    numero = int(carta[:-1])  # quitar el palo
    if numero <= 7:
        return numero
    else:
        return 0.5

# 5. Probar la función con varios ejemplos
print("Valor de 5C:", valor_carta("5C"))
print("Valor de 12O:", valor_carta("12O"))

# 6. Función para calcular el valor total de una mano
def valor_mano(mano):
    return sum(valor_carta(c) for c in mano)

# 7. Probar con manos de ejemplo
mano1 = ["5C", "12O"]  # 5 + 0.5 = 5.5
mano2 = ["7E", "3O"]   # 7 + 3 = 10
print("Valor mano 1:", valor_mano(mano1))
print("Valor mano 2:", valor_mano(mano2))
