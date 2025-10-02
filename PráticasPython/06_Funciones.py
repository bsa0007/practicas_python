def valor_carta(carta):
    numero = int(carta[:-1])  # quitar palo
    if numero <= 7:
        return numero
    else:
        return 0.5

print(valor_carta("5O"))   # 5
print(valor_carta("12E"))  # 0.5
