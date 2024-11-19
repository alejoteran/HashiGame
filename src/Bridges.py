import re
from grafo import Grafo

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
matriz_a_grafo = [
    ['2', '-', '3', '-', '-', '-', '4', '-', '-', '-', '2', ' ', ' '],
    ['|', ' ', '|', ' ', ' ', ' ', 'H', ' ', ' ', ' ', '|', ' ', '2'],
    ['|', ' ', '|', ' ', ' ', ' ', 'H', ' ', ' ', ' ', '|', ' ', 'H'],
    ['1', ' ', '1', ' ', ' ', ' ', 'H', ' ', '1', '-', '3', ' ', '3'],
    [' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', '|', ' ', '|'],
    ['2', '=', '=', '=', '=', '=', '8', '=', '=', '=', '5', '-', '2'],
    [' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', '|', ' ', ' '],
    ['3', '-', '-', '-', '3', ' ', 'H', ' ', ' ', ' ', '|', ' ', '1'],
    ['H', ' ', ' ', ' ', 'H', ' ', 'H', ' ', ' ', ' ', '|', ' ', '|'],
    ['H', ' ', ' ', ' ', '2', ' ', 'H', ' ', ' ', ' ', '3', '=', '4'],
    ['H', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', '|'],
    ['3', '-', '-', '-', '-', '-', '3', ' ', '1', '-', '-', '-', '2']
]
regex_conexiones = r'[^-=|H]'

def nombrar_nodos(matriz_numeros):
    nombre = 97
    for i in range(len(matriz_numeros)):            # Bucle sobre las filas
        for j in range(len(matriz_numeros[i])):
            if matriz_numeros[i][j].isdigit(): #verifica que esta en una isla
                matriz_numeros[i][j] = chr(nombre)
                nombre += 1

    return matriz_numeros

def generar_grafo(matriz_a_grafo):
    grafo_generado = Grafo()
    filas = len(matriz_a_grafo)
    columnas = len(matriz_a_grafo[0])

    matriz_a_grafo = nombrar_nodos(matriz_a_grafo)

    for i in range(filas):
        for j in range(columnas):
            # Si encontramos un nodo (letra) y no es 'H'
            if matriz_a_grafo[i][j].isalpha() and matriz_a_grafo[i][j] != 'H':
                nodo_actual = matriz_a_grafo[i][j]

                # Verificar conexiones horizontales
                if j + 1 < columnas and matriz_a_grafo[i][j + 1] in ['-', '=']:
                    k = j + 2
                    # Buscar el siguiente nodo
                    while k < columnas and (not matriz_a_grafo[i][k].isalpha() or matriz_a_grafo[i][k] == 'H'):
                        k += 1
                    if k < columnas and matriz_a_grafo[i][k].isalpha() and matriz_a_grafo[i][k] != 'H':
                        nodo_vecino = matriz_a_grafo[i][k]
                        grafo_generado.agregar_arista(nodo_actual, nodo_vecino)

                # Verificar conexiones verticales
                if i + 1 < filas and matriz_a_grafo[i + 1][j] in ['|', 'H']:
                    k = i + 2
                    # Buscar el siguiente nodo
                    while k < filas and (not matriz_a_grafo[k][j].isalpha() or matriz_a_grafo[k][j] == 'H'):
                        k += 1
                    if k < filas and matriz_a_grafo[k][j].isalpha() and matriz_a_grafo[k][j] != 'H':
                        nodo_vecino = matriz_a_grafo[k][j]
                        grafo_generado.agregar_arista(nodo_actual, nodo_vecino)

    for fila in matriz_a_grafo:
        print(fila)

    print(grafo_generado.mostrar_grafo())

    if grafo_generado.es_conexo():
        print("El grafo es conexo.")
        return True
    else:
        print("El grafo no es conexo.")
        return False



def leer_archivo(nombre_archivo):
    matriz_con_espacios = []

    with open(nombre_archivo, 'r') as archivo:
        # Leer la primera línea que contiene el tamaño de la matriz
        tamano = archivo.readline().strip()
        filas, columnas = map(int, tamano.split(','))  # Obtener el número de filas y columnas

        # Leer las siguientes líneas que contienen los datos de la matriz
        matriz = [list(linea.strip()) for linea in archivo]  # Convertir cada línea en una lista de caracteres

    # Generar la matriz con espacios vacíos entre cada casilla
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            # Reemplazar '0' con espacio
            if elemento == '0':
                nueva_fila.append(' ')
            else:
                nueva_fila.append(elemento)
            nueva_fila.append(' ')  # Agregar espacio entre los elementos

        # Agregar la fila generada con espacios
        matriz_con_espacios.append(nueva_fila[:-1])  # Eliminar el último espacio innecesario

        # Agregar una fila adicional de espacios en blanco del mismo tamaño que la fila anterior
        fila_vacia = [' ' for _ in nueva_fila[:-1]]  # Crear una fila de espacios
        matriz_con_espacios.append(fila_vacia)

    # Eliminar la última fila vacía si no se desea al final de la matriz
    matriz_con_espacios.pop()

    return matriz_con_espacios



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
                    return False

            if matriz[i][j] == '=':
                if  (j > 0 and (matriz[i][j - 1] == '=' or matriz[i][j - 1] in numeros)) and \
                    (j < columnas - 1 and (matriz[i][j + 1] == '=' or matriz[i][j + 1] in numeros)):
                    continue
                else:
                    print(f"Error en ({i}, {j}): con =")
                    return False


            if matriz[i][j] == '|':
                if  (i > 0 and (matriz[i - 1][j] == '|' or matriz[i - 1][j] in numeros)) and \
                    (i < filas - 1 and (matriz[i + 1][j] == '|' or matriz[i + 1][j] in numeros)):
                    continue
                else:
                    print(f"Error en ({i}, {j}): con |")
                    return False

            if matriz[i][j] == 'H':
                if  (i > 0 and (matriz[i - 1][j] == 'H' or matriz[i - 1][j] in numeros)) and \
                    (i < filas - 1 and (matriz[i + 1][j] == 'H' or matriz[i + 1][j] in numeros)):
                    continue
                else:
                    print(f"Error en ({i}, {j}): con H")
                    return False

    return True


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


def escribir_matriz_en_archivo(ruta_archivo, matriz):
    with open(ruta_archivo, 'w') as archivo:
        for fila in matriz:
            archivo.write(''.join(fila) + '\n')  # Unir la lista en una cadena y escribirla



def validar_solucion(solucion):
    for i in range(len(solucion)):
        if(solucion[i][0] != solucion[i][1]):
            #print(f"PERDIO le faltan conexiones: a la isla {solucion[i][0]} tiene {solucion[i][1]} conexiones")
            return False
    #print("GANÓ eeee")
    return True



if __name__ == '__main__':
    ## Ejemplo de uso
    nombre_archivo = 'm2.txt'
    matriz = leer_archivo(nombre_archivo)

    # Mostrar la matriz cuadrada
    for fila in matriz:
        print(*fila)

    #Generar archivo de prueba
    escribir_matriz_en_archivo("generado.txt", matriz)

    print('-------------------------------------------------------')
    #Generar grafo a partir de matriz solucionada
    generar_grafo(matriz_a_grafo)

    #validar_matriz(matriz)

    #solucion = validar_conexiones_necesarias(matriz)

    #validar_solucion(solucion)



def jugador_automatico(matriz_inicial):

    import copy

    matriz = copy.deepcopy(matriz_inicial)
    filas, columnas = len(matriz), len(matriz[0])

    def dentro_limites(x, y):
        return 0 <= x < filas and 0 <= y < columnas


    def encontrar_islas():
        return [(x, y) for x in range(filas) for y in range(columnas) if matriz[x][y].isdigit()]

    def vecinos_isla(x, y):
        vecinos = []
        for i in range(x - 1, -1, -1):  # Arriba
            if matriz[i][y] != ' ':
                if matriz[i][y].isdigit():
                    vecinos.append((i, y))
                break
        for i in range(x + 1, filas):  # Abajo
            if matriz[i][y] != ' ':
                if matriz[i][y].isdigit():
                    vecinos.append((i, y))
                break
        for j in range(y - 1, -1, -1):  # Izquierda
            if matriz[x][j] != ' ':
                if matriz[x][j].isdigit():
                    vecinos.append((x, j))
                break
        for j in range(y + 1, columnas):  # Derecha
            if matriz[x][j] != ' ':
                if matriz[x][j].isdigit():
                    vecinos.append((x, j))
                break
        return vecinos

    def solucion_completa():
        return all(int(matriz[x][y]) == 0 for x, y in islas)

    def verificar_numeros_negativos():
        """Devuelve True si hay algún número negativo en la matriz."""
        for fila in matriz:
            for celda in fila:
                if celda.isdigit() and int(celda) < 0:
                    return True
        return False

    def conectar_islas(x1, y1, x2, y2, tipo_puente):
        # Guardamos una copia de la matriz antes de intentar modificarla
        matriz_backup = copy.deepcopy(matriz)

        if x1 == x2:  # Horizontal
            paso = 1 if y2 > y1 else -1
            for j in range(y1 + paso, y2, paso):
                if matriz[x1][j] not in [' ', '-', '=']:
                    return False
            for j in range(y1 + paso, y2, paso):
                matriz[x1][j] = '-' if tipo_puente == 1 else '='
        elif y1 == y2:  # Vertical
            paso = 1 if x2 > x1 else -1
            for i in range(x1 + paso, x2, paso):
                if matriz[i][y1] not in [' ', '|', 'H']:
                    return False
            for i in range(x1 + paso, x2, paso):
                matriz[i][y1] = '|' if tipo_puente == 1 else 'H'
        else:
            return False

        matriz[x1][y1] = str(int(matriz[x1][y1]) - tipo_puente)
        matriz[x2][y2] = str(int(matriz[x2][y2]) - tipo_puente)

        # Verificar si hay números negativos en la matriz
        if verificar_numeros_negativos():
            # Si encontramos números negativos, revertimos la matriz a su estado anterior
            matriz[:] = matriz_backup[:]
            return False
        return True

    def desconectar_islas(x1, y1, x2, y2, tipo_puente):
        if x1 == x2:  # Horizontal
            paso = 1 if y2 > y1 else -1
            for j in range(y1 + paso, y2, paso):
                matriz[x1][j] = ' '
        elif y1 == y2:  # Vertical
            paso = 1 if x2 > x1 else -1
            for i in range(x1 + paso, x2, paso):
                matriz[i][y1] = ' '
        matriz[x1][y1] = str(int(matriz[x1][y1]) + tipo_puente)
        matriz[x2][y2] = str(int(matriz[x2][y2]) + tipo_puente)


    def backtrack():
        if solucion_completa():
            return True
        for x, y in islas:
            if int(matriz[x][y]) > 0:
                vecinos = vecinos_isla(x, y)
                for vx, vy in vecinos:
                    for tipo_puente in [1, 2]:
                        if conectar_islas(x, y, vx, vy, tipo_puente):
                            if backtrack():
                                return True
                            desconectar_islas(x, y, vx, vy, tipo_puente)
        return False

    islas = encontrar_islas()
    if backtrack():
        return matriz
    else:
        return None