'''
El siguiente ejemplo trata de dividir los dos números escritos por el usuario. Se producirá un error si
el segundo número es 0, y lo mostraremos en el bloque Except: 
'''

try:
    n1 = int(input("Escribe el dividendo:\n"))
    n2 = int(input("Escribe el divisor:\n"))
    resultado = n1 / n2
    print(f"El resultado de la división es: {resultado}")
except Exception as e:
    print("Error", str(e))

'''
Tambien se pueden provocar o lanzar excepciones en un momento determinado con la instrucción Raise. Esto permite, entre otras cosas,
centralizar los errores producidos en un único punto. Por ejemplo, si no quisieramos dividir números negativos en el ejemplo anterior
podríamos provocar una excepción dentro del Try para que se capture:   
'''

try:
    n1 = int(input("Escribe el dividendo:\n"))
    n2 = int(input("Escribe el divisor:\n"))
    if n1 < 0 or n2 < 0:
        raise Exception("No se admiten numeros negativos.")
    resultado = n1 / n2
    print("El resultado es:", resultado)
except Exception as e:
    print("Error:", str(e))