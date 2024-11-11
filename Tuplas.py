calle = input("Introduce tu calle: ")
numeroPuerta = int(input("Introduce tu número de puerta: "))
numeroPiso = int(input("Introduce tu número de piso: "))
direccionPostal = calle, numeroPuerta, numeroPiso

print(f"La calle es {direccionPostal[0]}, la puerta es {direccionPostal[1]} y el piso es {direccionPostal[2]}")