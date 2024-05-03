edad = int(input("Digite la edad del cliente: "))
if edad < 4 : 
    val = "entra gratis"
elif edad <= 18 :
    val = "debe pagar 5$"
elif edad > 18 : 
    val = "debe pagar 10$"
print(f"El cliente {val}")