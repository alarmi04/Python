def mcd(a, b):

    if a < b:
        a, b = b, a

    while b != 0:
        resto = a % b
        a, b = b, resto

    return a

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


print(mcd(20, 12))

for numero in range(51):
    if es_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
