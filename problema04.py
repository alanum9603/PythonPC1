num = int(round(float(input("Digite un número entero positivo (no puede ser 0): ")), 0))
if num == 0 :
    num += 1
    print(f"el número no puede ser 0, será pasado a 1 -> {num}")
elif num < 0 :
    num *= -1
    print(f"el número no puede ser negativo, será pasado a positivo -> {num}")
suma = int(num * (num + 1) /2)
print(f"suma de los primeros numeros enteros positivos: {suma}")