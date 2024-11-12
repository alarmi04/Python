def es_lista_valida(numeros):
    if len(numeros) != 6:
        print("La lista NO es válida: Debe contener exactamente 6 números.")
        return False
    if any(num < 1 or num > 49 for num in numeros):
        print("La lista NO es válida: Hay números menores que 1 o mayores que 49.")
        return False
    if len(numeros) != len(set(numeros)):
        print("La lista NO es válida: Hay números repetidos.")
        return False
    return True


entrada = input("Introduce los 6 números de la lotería separados por espacios:\n")
numeros = list(map(int, entrada.split()))
numeros.sort()
print(numeros)
if es_lista_valida(numeros):
    print("La lista es válida.")
else:
    print("La lista NO es válida.")
