numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

def leer_archivo(nombre_archivo):
    matriz = []
    max_len = 0

    # Leer todas las líneas del archivo y determinar la longitud máxima
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.rstrip('\n')  # Solo eliminar saltos de línea, no espacios
            max_len = max(max_len, len(linea))  # Encontrar la longitud máxima de las líneas
            matriz.append(list(linea))

    # Ajustar todas las filas a la longitud máxima con espacios
    for i in range(len(matriz)):
        if len(matriz[i]) < max_len: #si el tamaño de la fila
            matriz[i] += [' '] * (max_len - len(matriz[i]))  # Crea lista espacios en blanco y añade al final

    return matriz


## Ejemplo de uso
nombre_archivo = 'solm1.txt'
matriz = leer_archivo(nombre_archivo)

# Mostrar la matriz cuadrada
for fila in matriz:
    print(fila)


def validar_matriz(matriz):
    global numeros
    filas = len(matriz)
    columnas = len(matriz[0])

    # Recorrer horizontalmente
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == '-':
                if  (j > 0 and (matriz[i][j - 1] == '-' or matriz[i][j - 1] in numeros)) and \
                    (j < columnas - 1 and (matriz[i][j + 1] == '-' or matriz[i][j + 1] in numeros)):
                    continue
                else:
                    print(f"Error en ({i}, {j}): con -")

            if matriz[i][j] == '=':
                if  (j > 0 and (matriz[i][j - 1] == '=' or matriz[i][j - 1] in numeros)) and \
                    (j < columnas - 1 and (matriz[i][j + 1] == '=' or matriz[i][j + 1] in numeros)):
                    continue
                else:
                    print(f"Error en ({i}, {j}): con =")


            if matriz[i][j] == '|':
                if  (i > 0 and (matriz[i - 1][j] == '|' or matriz[i - 1][j] in numeros)) and \
                    (i < filas - 1 and (matriz[i + 1][j] == '|' or matriz[i + 1][j] in numeros)):
                    continue
                else:
                    print(f"Error en ({i}, {j}): con |")

            if matriz[i][j] == 'H':
                if  (i > 0 and (matriz[i - 1][j] == 'H' or matriz[i - 1][j] in numeros)) and \
                    (i < filas - 1 and (matriz[i + 1][j] == 'H' or matriz[i + 1][j] in numeros)):
                    continue
                else:
                    print(f"Error en ({i}, {j}): con H")

    return


validar_matriz(matriz)


#que cada isla tenga las conexiones necesarias
def validar_conexiones_necesarias(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    solucion = []

    # Recorrer horizontalmente
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] in numeros:    #estoy en la isla matriz[i][j]
                suma = 0

                if i > 0 and matriz[i - 1][j] == '|':
                    suma += 1
                if i < filas - 1 and matriz[i + 1][j] == '|':
                    suma += 1
                if i > 0 and matriz[i - 1][j] == 'H':
                    suma += 2
                if i < filas - 1 and matriz[i + 1][j] == 'H':
                    suma += 2
                if j > 0 and matriz[i][j - 1] == '-':
                    suma += 1
                if j < columnas - 1 and matriz[i][j + 1] == '-':
                    suma += 1
                if j > 0 and matriz[i][j - 1] == '=':
                    suma += 2
                if j < columnas - 1 and matriz[i][j + 1] == '=':
                    suma += 2

                #print (f"La isla {matriz[i][j]} tiene {suma} conexiones")
                solucion.append((int(matriz[i][j]), int(suma))) #lista de tuplas
    return solucion

solucion = validar_conexiones_necesarias(matriz)


def validar_solucion(solucion):
    for i in range(len(solucion)):
        if(solucion[i][0] != solucion[i][1]):
            print(f"PERDIO le faltan conexiones: a la isla {solucion[i][0]} tiene {solucion[i][1]} conexiones")
    return


validar_solucion(solucion)
