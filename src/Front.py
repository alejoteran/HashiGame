import tkinter as tk
from tkinter import messagebox
import Bridges

SYMBOLS = [' ', '=', '-', '|', 'H', '']
SYMBOLS_NUM = [' ', '=', '-', '|', 'H', ''] + [str(i) for i in range(10)]


# Función para leer el archivo y crear la matriz
def leer_archivo_generado(archivo):
    with open(archivo, 'r') as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    matriz = [list(line) for line in lines]
    num_filas = len(matriz)
    num_columnas = max(len(line) for line in matriz)
    return matriz, num_filas, num_columnas


# Función para actualizar el grid con la solución del jugador automático
def jugador_automatico():
    solucion = Bridges.jugador_automatico()  # Llama a la función que genera la solución
    if solucion:
        for i, fila in enumerate(solucion):
            for j, valor in enumerate(fila):
                if celdas[i][j]['state'] != 'readonly':  # No modificar celdas de solo lectura
                    celdas[i][j].delete(0, tk.END)
                    celdas[i][j].insert(0, valor)
        messagebox.showinfo("Jugador Automático", "¡La solución se ha generado automáticamente!")
    else:
        messagebox.showerror("Error", "No se pudo generar una solución automática.")


# Función para guardar el estado actual de la cuadrícula en un archivo
def guardar_estado(archivo, grid_state):
    matriz_bridges = [[' ' for _ in range(len(grid_state[0]))] for _ in range(len(grid_state))]
    for i, fila in enumerate(grid_state):
        for j, cell in enumerate(fila):
            matriz_bridges[i][j] = cell.get() if cell.get() != "" else ' '

    matriz_valida = Bridges.validar_matriz(matriz_bridges)
    solucion = Bridges.validar_conexiones_necesarias(matriz_bridges)
    ganador = Bridges.validar_solucion(solucion)

    if ganador:
        conectado = Bridges.generar_grafo(matriz_bridges)
        if matriz_valida and ganador and conectado:
            with open(archivo, 'w') as f:
                for fila in grid_state:
                    fila_str = ''.join(cell.get() if cell.get() != "" else ' ' for cell in fila)
                    f.write(fila_str + '\n')
            messagebox.showinfo("Éxito", "¡Has ganado!")
        else:
            messagebox.showinfo("Información", "No se cumplieron todas las reglas del juego.")
    else:
        messagebox.showerror("Error", "La solución no es válida.")


# Función para validar si los datos ingresados son válidos
def validar_simbolo(simbolo):
    return simbolo in SYMBOLS


def actualizar_celda(event, row, col):
    nuevo_valor = celdas[row][col].get()
    if not validar_simbolo(nuevo_valor):
        messagebox.showerror("Error", f"Valor no permitido: {nuevo_valor}.")
        celdas[row][col].delete(0, tk.END)


# Función de guardar con validación
def guardar_con_validacion():
    if all(validar_simbolo(celda.get()) for fila in celdas for celda in fila):
        guardar_estado("estado_guardado.txt", celdas)
    else:
        messagebox.showerror("Error", "Hay valores no permitidos en la cuadrícula.")


if __name__ == '__main__':
    Bridges.leer_archivo("m.txt")
    archivo = "generado.txt"
    matriz, num_filas, num_columnas = leer_archivo_generado(archivo)

    root = tk.Tk()
    root.title("Bridges Game")

    frame = tk.Frame(root)
    frame.pack()

    celdas = [[None for _ in range(num_columnas)] for _ in range(num_filas)]
    for row in range(num_filas):
        for col in range(num_columnas):
            entry = tk.Entry(frame, width=4, justify='center')
            if col < len(matriz[row]) and matriz[row][col] != ' ':
                entry.insert(0, matriz[row][col])
                entry.config(state='readonly')
            else:
                entry.bind('<KeyRelease>', lambda e, r=row, c=col: actualizar_celda(e, r, c))
            entry.grid(row=row, column=col)
            celdas[row][col] = entry

    save_button = tk.Button(root, text="Guardar", command=guardar_con_validacion)
    save_button.pack()

    auto_button = tk.Button(root, text="Jugador Automático", command=jugador_automatico)
    auto_button.pack()

    root.mainloop()
