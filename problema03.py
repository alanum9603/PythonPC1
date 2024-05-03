peso_payasos = 112
peso_munecas = 75
num_payasos = int(input("Digite el número de payasos vendidos: "))
num_munecas = int(input("Digite el número de muñecas vendidas: "))
peso_total = peso_payasos * num_payasos + peso_munecas * num_munecas
print(f"Peso total del envío: {peso_total}")