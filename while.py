total_pares = 0
total_impares = 0
num = 0
while True:
    num = int(input("Ingrese un número positivo: "))
    if num == 0:
        break
    pares = 0
    impares = 0
    num_str = str(num)
    for digito in num_str:
        if int(digito)%2==0:
            pares += 1
        else:
            impares += 1
    print(f"El número {num} tiene {pares} dígito(s) par(es) y {impares} dígito(s) impar(es).")
    total_pares += pares
    total_impares += impares
print(f"Total de dígitos pares leídos: {total_pares}")
print(f"Total de dígitos impares leídos: {total_impares}")