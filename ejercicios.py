#00_Hello

#Esto es un comentario
#Hola Python
print("Hello Python")
print('Hola Python')

print(type(True))

"""
esto es un comentario
 de
 tres lineas

"""

#01_variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False

print(my_bool_variable)

print(my_string_variable,str(my_int_variable),my_bool_variable)

print("Este es el valor de:", my_bool_variable)
# Algunas funciones del sistema
print(len(my_int_to_str_variable))

#Variables en una sola línea !Cuidado con abusar de esta sintaxis!
name, surname, alias, age  ="Brian", "Solano", "Hiwork", 28
print("Me llamo:",name,surname,"Mi edad es:", age )

#Cambiamos su tipo

name = 35
age = "Brian"
print(name)
print(age)

# Forzamos el tipo

address: str = "Mi dirección"
address = 32
print(address)

#02_Operadores

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

#03_Condicional_Simple

numero = 6
if numero > 7:
    print("Mayor que siete")
else:
    print("No es mayor que siete")

#04_Bucles

# Imprime los números del 1 al 10
for i in range(1, 11):
    print(i)

#05_Listas

cartas = ["1O", "2O", "3O", "4O"]
print("Tengo", len(cartas), "cartas")
print("La primera carta es:", cartas[0])


#06_Funciones

def valor_carta(carta):
    numero = int(carta[:-1])  # quitar palo
    if numero <= 7:
        return numero
    else:
        return 0.5

print(valor_carta("5O"))   # 5
print(valor_carta("12E"))  # 0.5

#07_Probabilidad_Simple

# Probabilidad de sacar un 5 en una baraja española de 40 cartas
casos_favorables = 4
casos_posibles = 40
prob = casos_favorables / casos_posibles
print("Probabilidad de sacar un 5:", prob)



