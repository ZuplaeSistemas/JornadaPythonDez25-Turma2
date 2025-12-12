# loops
# estruturas de repeticao

print('Imprimindo range')

for numero in range(0, 6):
    print(numero)

print('fim impresao')

numeros = [10, 5, 9, 7, 8, 18, 49] # list
soma = 0
for numero in numeros:
    soma = soma + numero
    print(f"{numero} - {soma}")