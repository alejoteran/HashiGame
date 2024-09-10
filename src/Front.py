import tkinter as tk

# Definimos el tamaño de la cuadrícula
GRID_SIZE = 13

# Símbolos que van cambiando con cada clic
SYMBOLS = [' ', '=', '-', '|', 'H']

# Creamos la ventana principal
root = tk.Tk()
root.title("Bridges Game")

# Creamos un marco para contener la cuadrícula
frame = tk.Frame(root)
frame.pack()

# Creamos una lista para almacenar los botones
buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
grid_state = [[SYMBOLS[0] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Matriz que almacena el estado actual


# Función para manejar los clics en los botones
def on_button_click(row, col):
    # Obtener el símbolo actual
    current_symbol = grid_state[row][col]

    # Encontrar el siguiente símbolo en el ciclo
    next_symbol = SYMBOLS[(SYMBOLS.index(current_symbol) + 1) % len(SYMBOLS)]

    # Actualizar la matriz y el botón
    grid_state[row][col] = next_symbol
    buttons[row][col].config(text=next_symbol)

    # Aquí puedes llamar a la lógica de backend para actualizar el estado del juego
    print(f"Posición ({row}, {col}) cambiado a: {next_symbol}")


# Crear botones en la cuadrícula
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        buttons[row][col] = tk.Button(frame, text=grid_state[row][col], width=4, height=2,
                                      command=lambda r=row, c=col: on_button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Iniciar la aplicación
root.mainloop()
