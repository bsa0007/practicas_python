#Variables

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