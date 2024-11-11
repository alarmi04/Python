numero = int(input("Introduce un número: "))
listaNumeros = []
while numero != 0:
    listaNumeros.append(numero)
    numero = int(input("Introduce otro número: "))

numeroBuscar = int(input("Que número quieres buscar: "))
print(f"El numero {numeroBuscar} tiene la posicion {listaNumeros.index(numeroBuscar)+1}")
  