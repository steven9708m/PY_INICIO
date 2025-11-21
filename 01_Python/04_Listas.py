### LISTAS ###
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [28, 45, 23, 18, 33]

print(my_list)
print(len(my_list))

my_other_list = [28, 1.73, "Steven Miranda"]
print(my_other_list)

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[2])
print(my_other_list[-2])
print(my_other_list[-1])
print(my_list.count(30))  # Cuenta cuántas veces aparece el valor 30 en la lista
print(my_list.count(28))  # Cuenta cuántas veces aparece el valor 28 en la lista

age, height, name = my_other_list
print(age)

print(my_list + my_other_list)  # Concatenación de listas