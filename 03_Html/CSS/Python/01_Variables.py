# VARIABLES

my_string_variable = "Primera variable"
print(my_string_variable) # Primera variable

my_int_variable = 8
print(my_int_variable) # 8

my_int_to_str_varuable = str (my_int_variable)
print(my_int_to_str_varuable) # 8
print(type(my_int_to_str_varuable)) # <class 'str'>

my_boolean_variable = True
print(my_boolean_variable) # True

print (type(print(my_string_variable, my_int_variable, my_boolean_variable, my_int_to_str_varuable)))
# concatenación de variables incorrecta

print("Este es el valor de:",my_int_to_str_varuable)

print(len(my_int_to_str_varuable))
#Algunas funciones del sistema

name, surname, alias, age = "Steven", "Miranda", "Mirandero", 27
#Variables en una sola línea

print ("Me llamo:", name, ', Mi apellido es:', surname, ', Mi alias es:', alias, ', Mi edad es:', age)

#Input de datos
'''first_name = input('What is your name: ')
age = input('How old are you? ')
print(first_name)
print(age)'''

#cambiamos el tipo de dato de la variable
name = 18
age = "Lucas"
print(name)
print(age)

#forzamos el cambio de tipo de dato
address: str = 'Mi dirección'
address = 10
print(type(address))

#str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int)) 