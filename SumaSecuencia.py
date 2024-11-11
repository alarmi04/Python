try: 
    numeros = input("Introduce una cadena de números separada por espacios:")
    numeros = numeros.strip()
    suma = numeros.split(" ")
    acu = 0
    for i in range(len(suma)):
        acu += int(suma[i])

    print(f"La suma de todos los numeros introducidos es {acu}")
except Exception as e:
    print("Error: ", str(e))

