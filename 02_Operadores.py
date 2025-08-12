"""OPERADORES ARITMETICOS"""

print('Suma: ', 1 + 2)                     # 3
print('Resta: ', 2 - 1)                    # 1
print('Multiplicación: ', 2 * 3)           # 6
print('División: ', 4 / 2)                 # 2.0  La división en Python devuelve número flotante
print('División: ', 6 / 2)                 # 3.0
print('División: ', 7 / 2)                 # 3.5
print('División sin el residuo: ', 7 // 2) # 3, devuelve sin decimales, sin el residuo
print('División sin el residuo: ', 7 // 3) # 2
print('Módulo: ', 3 % 2)                   # 1, devuelve el residuo
print('Exponenciación: ', 2 ** 3)          # 8 significa 2 * 2 * 2

"""OPERADORES ARITMETICOS CON ASIGNACIÓN"""
print('Operador de asignación: ', 5)       # Asignación de valor
print('Operador de asignación: ', 5 + 2)   # Asignación de valor con suma
print('Operador de asignación: ', 5 - 2)   # Asignación de valor con resta
print('Operador de asignación: ', 5 * 2)   # Asignación de valor con multiplicación
print('Operador de asignación: ', 5 / 2)   # Asignación de valor con división
print('Operador de asignación: ', 5 // 2)  # Asignación de valor con división sin residuo
print('Operador de asignación: ', 5 % 2)   # Asignación de valor con módulo
print('Operador de asignación: ', 5 ** 2)  # Asignación de valor con exponenciación         
print('Operador de asignación: ', 5 + 2 * 3) # 11, respeta la jerarquía de operaciones
print('Operador de asignación: ', (5 + 2) * 3) # 21, respeta la jerarquía de operaciones con paréntesis

"""OPERADORES DE COMPARACIÓN"""
print(3 > 2 and 4 > 3) # Verdadero - porque ambas expresiones son verdaderas
print(3 > 2 and 4 < 3) # Falso - porque la segunda expresión es falsa
print(3 < 2 and 4 < 3) # Falso - porque ambas expresiones son falsas
print('Verdadero y Verdadero: ', True and True)
print(3 > 2 or 4 > 3)  # Verdadero - porque ambas expresiones son verdaderas
print(3 > 2 or 4 < 3)  # Verdadero - porque una de las expresiones es verdadera
print(3 < 2 or 4 < 3)  # Falso - porque ambas expresiones son falsas
print('Verdadero o Falso:', True or False)
print(not 3 > 2)     # Falso - porque 3 > 2 es verdadero, entonces not True da Falso
print(not True)      # Falso - Negación, el operador not convierte verdadero en falso
print(not False)     # Verdadero
print(not not True)  # Verdadero
print(not not False) # Falso

# 4. OPERADORES LÓGICOS
# =============================
print("True and True:", True and True)    # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)              # False
print("not False:", not False)            # True

print("\n=============================")

# =============================
# 5. OPERADORES DE PERTENENCIA
# =============================
lista = [1, 2, 3, 4, 5]
print("¿2 in lista?", 2 in lista)          # True
print("¿10 in lista?", 10 in lista)        # False
print("¿10 not in lista?", 10 not in lista) # True

texto = "hola mundo"
print("'hola' in texto?", "hola" in texto) # True
print("'adios' not in texto?", "adios" not in texto) # True

print("\n=============================")

# ================================
# 6. OPERADORES DE IDENTIDAD
# ===============================
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("¿a is b?", a is b)       # True (apuntan al mismo objeto)
print("¿a is c?", a is c)       # False (aunque tengan el mismo contenido)
print("¿a is not c?", a is not c) # True

print("\n=============================")

# =============================
# 7. OPERADORES BIT A BIT
# =============================
x = 5  # en binario: 0101
y = 3  # en binario: 0011

print("x & y:", x & y)   # AND: 0101 & 0011 = 0001 (1)
print("x | y:", x | y)   # OR: 0101 | 0011 = 0111 (7)
print("x ^ y:", x ^ y)   # XOR: 0101 ^ 0011 = 0110 (6)
print("~x:", ~x)         # NOT: ~0101 = -(5+1) = -6
print("x << 1:", x << 1) # Desplaza bits a la izquierda: 0101 -> 1010 (10)
print("x >> 1:", x >> 1) # Desplaza bits a la derecha: 0101 -> 0010 (2)

print("\n¡Todos los operadores han sido demostrados!")