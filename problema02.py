consumo = float(input("Digite el costo en soles de su consumo en el restaurante: "))
porcentaje = float(input("Digite el porcentaje de propina que desea dejar al mesero: "))
propina = round(consumo * porcentaje / 100, 2)
print(f"Cantidad de dinero a dejar como propina: S/{propina}")