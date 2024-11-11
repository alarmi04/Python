"""
Una lista en python sera una secuencia de elementos que pueden ser de distintos tipos. Se representa con los elementos
separados por comas, entre corchetes. Por ejemplo:

"""

datos = ["Nacho", "Pepe", 2015, 2013]

"""
Además, podemos crear una lista sin valores iniciales, usando corchetes vacíos o la instrucción List:

datos = []
datos = List()
"""

"""
Con esta instruccion se imprimira por pantalla el segundo elemento de la lista, si en vez de poner 1 ponemos -1 
se imprimiria desde el final de la lista en este caso seria 2013.
"""
print(datos[1])  # Pepe
print(datos)  # ['Nacho', 'Pepe', 2015, 2013]


"""
Para recorrer los elementos de una lista, podemos utilizar un for que recorra sus elementos…
"""
for elemento in datos:
    print(elemento)
"""
O tambien un for que recorra las posiciones del array.
"""
for i in range(0, len(datos)):
    print(datos[i])

"""
Lista multidimensionales son listas que contienen otras listas.

datos = [
    ["Nacho", 40, 233],
    ["Pepe", 70, 231],
]

En estas listas para querer sacar el indice de Nacho habra q poner el indice de la lista y luego del dato,
en este caso datos[0][0], otro ejemplo datos[1][2] (Indice de 231)
"""

"""
Si queremos añadir un elemento al final de la lista usamos la instruccion append, en el caso de querer insertar un elemento
en una posicion determinada, usariamos la instruccion insert, indicando en que posicion queremos insertar y el dato a insertar.

Tambien podriamos actualizar el valor de un dato de la lista, simplemente indicando su posicion y el nuevo valor que queremos asignar.

Y finalmente si queremos eliminar un dato de la lista, usamos la instruccion "del", seguida del elemento que queremos eliminar, de otra
manera podemos usar la instruccion "remove" de la propia lista, indicando el dato que queremos borrar.

datos = [1, 2, 3]
datos.append(1000)      # [1, 2, 3, 1000]
datos.insert(1, 20)     # [1, 20, 2, 3, 1000]
del datos[2]            # [1, 20, 3, 1000]
datos.remove(20)        # [1, 3, 1000]

"""

'''
OTRAS OPERACIONES CON LISTAS

La instruccion len(lista) devuelve el número de elementos actualmente almacenado en la lista, sirve tanto para listas normales como 
multidimensionales.

datos = [1, 2, 3, 4]
print(len(datos))       # 4
 datos2 = [
    [1, 2, 3],
    [4, 5, 6, 7]
]
print(len(datos2))      # 2 (cantidad de filas)
print(len(datos2[0]))   # 3 (cantidad de datos de la primera fila)

'''