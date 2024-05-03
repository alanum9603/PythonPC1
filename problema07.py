num1 = int(input("Digite un número: "))
num2 = int(input("Digite un número: "))
menu = int(input("Digite un número conforme a que desea realizar\n1 -> Suma\n2 -> Resta (número 1 - número 2)\n3 -> Multiplicación\nDigite a continuación: "))
if menu == 1 : 
    op = num1 + num2
elif menu == 2 : 
    op = num1 - num2
elif menu == 3 : 
    op = num1 * num2
else :
    op = "No se digitó un número conforme al menú de opciones"
print(f"Resultado: {op}")