inp = input("Digite una lista, separe los valores por coma: ")
list =  inp.split(", ")
list =  ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
list.pop(5)
list.pop(4)
list.pop(0)
print(list)