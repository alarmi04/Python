def calcular_mcd(n1, n2):

    if n1 < n2:
        n1, n2 = n2, n1

    while n2 != 0:
        resto = n1 % n2
        n1, n2 = n2, resto

    return n1

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

mcd = calcular_mcd(n1, n2)
print(f"El MCD de {n1} y {n2} es: {mcd}")
