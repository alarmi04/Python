precios = int(input("Introduce un precio: "))
acu = int(0)
while precios != 0:
    acu += precios
    precios = int(input("Introduce un precio: "))
print("El total de la factura es %.2f" % acu)