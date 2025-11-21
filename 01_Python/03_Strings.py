#===================
# STRINGS EN PYTHON
#===================

my_string = "Mi primer string en Python"
my_other_string = 'Mi otro string en Python'

print(len(my_string))  # Imprime la longitud del string
print(len(my_other_string))  # Imprime la longitud del otro string

print(my_string + " y " + my_other_string)  # Concatenación de strings

my_new_line_string = "Este es un string \ncon un salto de línea"
print(my_new_line_string)  # Imprime el string con salto de línea

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string) # Imprime el string con tabulación

my_scaped_string = "Este es un string \nescapado"
print(my_scaped_string)  # Imprime el string escapado

# formateo

name, surname, age = "Steven", "Miranda", 28

print("Mi nombre es %s %s y tengo %d años" % (name, surname, age))  # Formateo con el operador %
print("Mi nombre es {} {} y tengo {} años".format(name,surname, age))  # Formateo con el método format
print(f"Mi nombre es {name} {surname} y tengo {age} años")  # Formateo con f-strings"

language = "Python"
reversed_language = language[::-1]
print(reversed_language)  # Imprime el string invertido

print(language.capitalize())  # Imprime el string con la primera letra en mayúscula
print(language.upper())  # Imprime el string en mayúsculas
print(language.lower())  # Imprime el string en minúsculas
print(language.count("t"))  # Imprime el número de veces que aparece 't' en el string
print(language.startswith("Py"))  # Imprime True si el string empieza con 'Py'
print(language.endswith("on"))  # Imprime True si el string termina con 'on'
print(language.replace("thon", "py"))  # Imprime el string con 'thon' reemplazado por 'py'
print(language.split("t"))  # Imprime una lista dividiendo el string por 't'
print("   Python   ".strip())  # Imprime el string sin espacios al inicio y al final
print("   Python   ".lstrip())  # Imprime el string sin espacios al inicio
print("   Python   ".rstrip())  # Imprime el string sin espacios al final
print(language.find("tho"))  # Imprime el índice donde empieza 'tho' en el string
print(language.index("y"))  # Imprime el índice donde está 'y' en el string