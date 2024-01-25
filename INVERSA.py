import numpy as np

# Mamani Jimenez Nayely Eymi 

print("Se calculara el det de A(2x2) para ver si es invertible y si lo es se calculadora su inversa")
filas, columnas = 2, 2


matrizA = []
for i in range(filas):
    matrizA.append([0] * columnas)


for fila in range(filas):
    for columna in range(columnas):
        matrizA[fila][columna] = int(
            input(f'Ingrese el valor en la posicion {fila}, {columna}:  '))

determinante = np.linalg.det(matrizA)
det = int(determinante)
print("El det de A es: ")
print(det)

if det != 0:
    print("Sabiendo que det A es distinto a O la matriz es invertible")
else:
    print("Sabiendo que det A es distinto igual a 0 la matriz NO es invertible")