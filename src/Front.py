import tkinter as tk
from tkinter import messagebox
import Bridges
SYMBOLS = [' ', '=', '-', '|', 'H', '']
SYMBOLS_NUM = [' ', '=', '-', '|', 'H', ''] + [str(i) for i in range(10)]


# Función para leer el archivo y crear la matriz
def leer_archivo_generado(archivo):
    with open(archivo, 'r') as f:
        lines = f.readlines()

    # Limpiar las líneas eliminando espacios en blanco a los lados y líneas vacías
    lines = [line.rstrip() for line in lines]

    # Crear una matriz a partir del archivo (incluyendo los espacios)
    matriz = [list(line) for line in lines]

    num_filas = len(matriz)
    num_columnas = max(len(line) for line in matriz)

    return matriz, num_filas, num_columnas



# Función para guardar el estado actual de la cuadrícula en un archivo
def guardar_estado(archivo, grid_state):
    #SE LLAMAN A LAS FUNCIONES DE BRIDGES

    # Suponiendo que grid_state es una lista bidimensional de celdas
    # Inicializa la matriz con el tamaño adecuado
    matriz_bridges = [[' ' for _ in range(len(grid_state[0]))] for _ in range(len(grid_state))]

    i = 0
    for fila in grid_state:
        fila_str = ''.join(cell.get() if cell.get() != "" else ' ' for cell in fila)
        for j in range(len(fila_str)):
            matriz_bridges[i][j] = fila_str[j]  # Asigna el valor de fila_str a la matriz
        i += 1

    # Imprimir la matriz resultante
    for fila in matriz_bridges:
        print(fila)


    matriz_valida = Bridges.validar_matriz(matriz_bridges) #RETORNA TRUE SI LAS CONEXIONES ESTAN BIEN
    solucion = Bridges.validar_conexiones_necesarias(matriz_bridges)#RETORNA LAS CONEXIONES DE CADA ISLA
    ganador = Bridges.validar_solucion(solucion) #RETORNA TRUE SI ESAS CONEXIONES SON CORRECTAS
    if (ganador):
        conectado = Bridges.generar_grafo(matriz_bridges)

        with open(archivo, 'w') as f:
            for fila in grid_state:
                fila_str = ''.join(cell.get() if cell.get() != "" else ' ' for cell in fila)
                f.write(fila_str + '\n')

        if matriz_valida and ganador and conectado:
            print("GANOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        else:
            print("PERDIOOOOOOOO")
    else:
        print("PERDIOOOOOOOO")

# Función para validar si los datos ingresados son válidos
def validar_simbolo(simbolo):
    return simbolo in SYMBOLS

def validar_simbolo_num(simbolo):
    return simbolo in SYMBOLS_NUM

# Función para actualizar el valor de una celda con validación
def actualizar_celda(event, row, col):
    nuevo_valor = celdas[row][col].get()
    if not validar_simbolo(nuevo_valor):
        messagebox.showerror("Error", f"Valor no permitido: {nuevo_valor}. Solo se permiten: {', '.join(SYMBOLS)}")
        celdas[row][col].delete(0, tk.END)  # Borrar contenido no permitido

# Función de guardar con validación
def guardar_con_validacion():
    if all(validar_simbolo_num(celda.get()) for fila in celdas for celda in fila):
        guardar_estado("estado_guardado.txt", celdas)
        messagebox.showinfo("Éxito", "El estado ha sido guardado exitosamente.")
    else:
        messagebox.showerror("Error", "Hay valores no permitidos en la cuadrícula.")



if __name__ == '__main__':
    # Cargar la matriz desde el archivo .txt
    Bridges.leer_archivo("m.txt")
    archivo = "generado.txt"  # Reemplaza con tu archivo
    matriz, num_filas, num_columnas = leer_archivo_generado(archivo)

    # Crear ventana principal
    root = tk.Tk()
    root.title("Bridges Game")

    # Crear marco para contener la cuadrícula
    frame = tk.Frame(root)
    frame.pack()

    # Crear celdas de entrada en el Canvas para cada celda de la matriz
    celdas = [[None for _ in range(num_columnas)] for _ in range(num_filas)]

    for row in range(num_filas):
        for col in range(num_columnas):
            entry = tk.Entry(frame, width=4, justify='center')

            # Verificar si la celda actual contiene un número
            if col < len(matriz[row]) and matriz[row][col] != ' ':
                entry.insert(0, matriz[row][col])  # Insertar el valor inicial desde el archivo
                entry.config(state='readonly')  # Hacer que esta celda sea de solo lectura
            else:
                entry.bind('<KeyRelease>',
                           lambda e, r=row, c=col: actualizar_celda(e, r, c))  # Validar al Kiriliz

            entry.grid(row=row, column=col)
            celdas[row][col] = entry

# Crear botón de "Guardar"
save_button = tk.Button(root, text="Guardar", command=guardar_con_validacion)
save_button.pack()

# Iniciar la aplicación
root.mainloop()