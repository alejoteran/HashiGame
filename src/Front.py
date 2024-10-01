import tkinter as tk
from tkinter import messagebox

SYMBOLS = [' ', '=', '-', '|', 'H', '']  + [str(i) for i in range(10)] # Símbolos permitidos

# Función para leer el archivo y crear la matriz
def leer_archivo(archivo):
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
    with open(archivo, 'w') as f:
        for fila in grid_state:
            fila_str = ''.join(cell.get() if cell.get() != "" else ' ' for cell in fila)
            f.write(fila_str + '\n')

# Función para validar si los datos ingresados son válidos
def validar_simbolo(simbolo):
    return simbolo in SYMBOLS

# Función para actualizar el valor de una celda con validación
def actualizar_celda(event, row, col):
    nuevo_valor = celdas[row][col].get()
    if not validar_simbolo(nuevo_valor):
        messagebox.showerror("Error", f"Valor no permitido: {nuevo_valor}. Solo se permiten: {', '.join(SYMBOLS)}")
        celdas[row][col].delete(0, tk.END)  # Borrar contenido no permitido

# Función de guardar con validación
def guardar_con_validacion():
    if all(validar_simbolo(celda.get()) for fila in celdas for celda in fila):
        guardar_estado("estado_guardado.txt", celdas)
        messagebox.showinfo("Éxito", "El estado ha sido guardado exitosamente.")
    else:
        messagebox.showerror("Error", "Hay valores no permitidos en la cuadrícula.")

# Cargar la matriz desde el archivo .txt
archivo = "generado.txt"  # Reemplaza con tu archivo
matriz, num_filas, num_columnas = leer_archivo(archivo)

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
        entry.grid(row=row, column=col)
        if col < len(matriz[row]) and matriz[row][col] != ' ':  # Check if the column index is within the valid range and not a space
            entry.insert(0, matriz[row][col])  # Insertar el valor inicial desde el archivo
        entry.bind('<FocusOut>', lambda e, r=row, c=col: actualizar_celda(e, r, c))  # Validar al salir del campo
        celdas[row][col] = entry

# Crear botón de "Guardar"
save_button = tk.Button(root, text="Guardar", command=guardar_con_validacion)
save_button.pack()

# Iniciar la aplicación
root.mainloop()