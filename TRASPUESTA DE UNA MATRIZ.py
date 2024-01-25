
# Mamani Jimenez Nayely Eymi 

print("Ingresar el tamanio de la matriz: ")
filas, columnas = int(input()), int(input()) 

matriz = []
for i in range(filas):
    matriz.append([0] * columnas)

for fila in range(filas):
    for columna in range(columnas):
        matriz[fila][columna] = int(
            input(f"Ingrese el valor en la posicion {fila}, {columna}:  "))

print("\nMatriz A\n")
for i in matriz:
    print(i)

filas2 = columnas
columnas2 = filas

matriz2 = []
for i in range(filas2):
    matriz2.append([0] * columnas2)

for fila in range(filas2):
    for columna in range(columnas2):
        matriz2[fila][columna] = matriz[columna][fila]

print('\nTranspuesta de A\n')
for i in matriz2:
    print(i)