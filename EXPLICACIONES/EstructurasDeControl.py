numero = int(input("Escribe un numero positivo: "))
if numero > 0:
    numero = numero + 1
    print("El siguiente número es: ", numero)
else:
    if numero < -10:
        print("El número es demasiado bajo.")
    else: 
        print("El numero no es positivo")
print("Fin del programa")

# If ternario
n = 7
par = True if n % 2 == 0 else False
print(f"{par}")

