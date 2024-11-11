'''
Crea un programa llamado DiccionarioTuplas.py donde le pidas al usuario que rellene direcciones 
de 4 usuarios, identificados por su clave que será el DNI. Así, para cada usuario rellenará dicho 
DNI, y luego los datos de la dirección como en el ejercicio anterior (nombre de calle, número de 
puerta y número de piso). Almacenará los datos en un diccionario (asociando cada DNI con su 
dirección) y luego le pedirá al usuario que escriba un DNI y mostrará los datos de su dirección, o el 
mensaje “El DNI no se encuentra almacenado” si no existe dicha clave.
'''
try:
    direcciones = {}

    for i in range(4):
        dni = input("Introduce tu DNI:")
        direccion = input("Introduce tu dirección:")
        puerta = int(input("Introduce tu puerta:"))
        piso = int(input("Introduce tu piso:"))
        direcciones[dni] = (dni, direccion, puerta, piso)

    buscarDatos = input("Introduce el DNI para mostrar sus datos:")
    if buscarDatos in direcciones:
        print(direcciones[buscarDatos])
    else:
        print("El dni no existe")
except Exception as e:
    print("Error", str(e))
