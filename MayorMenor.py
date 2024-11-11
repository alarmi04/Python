repeticion = int(input("Dime cuántos números vas a introducir:\n"))

mayor = None
menor = None


print(f"Escribe {repeticion} números:")
for i in range(repeticion):
    numero = int(input())
    if mayor is None or numero > mayor:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero

print(f"El mayor es {mayor}")
print(f"El menor es {menor}")
