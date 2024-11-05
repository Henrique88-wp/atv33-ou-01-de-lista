#mostre-me as seguintes listas derivadas de:
#[0,1,2,3,4,5,6,7,8,,9,10,11,12,13,14,15]
#intervalo de 1 a 9.
#intervalo de 8 a 13.
#números pares.
#números impares.
#todos os multiplos de 2, 3 e 4.
#lista reversa.
#razão enre o intervalo de 10  a 15 pelo intervalo de 3 a 9 em float.




lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in range(1):
    print(f"Intervalo de 1 a 9: {lista[2:9]}")



print("Outro intervalo:")
for i in range(1):
    print(f"O intervalo de 8 a 13 é: {lista[8:13]}")



print("Números pares:")
pares = [num for num in lista if num % 2 == 0]
print(f"Os números pares que estão na lista são: {pares}")



print("Números impares:")
impares = [num for num in lista if num % 2 == 1]
print(f"Os números impares que está na lista é: {impares}")



print("Todos os números multiplos de 2,3,4")


print("Número 02:")
numero_2 = [num for num in lista if num % 2 == 0]
print(f"Os números múltipos de 2 é: {numero_2}")



print("Número 03:")
numero_3 = [num for num in lista if num % 2 ==1]
print(f"Todos os números múltiplos de 3 é: {numero_3}")



print("Número 04:")
numero_4 = [num for num in lista if num % 4 == 0]
print(f"Os números múltiplos de 4 é: {numero_4}")


print("Revertendo a lista:")
lista.reverse()
print(f"A lista reversa fica: {lista}")



print("Comprimento do intervalo de 10 a 15 e 3 a 9")

a = (10 - 15)
b = (3 - 9)
c = (a / b)
print(c)