import Bridges


#sera que es poner una cosa y llamar a las de verificacion para ver que no halla problema en agregarla???

#mirar como esta funcionando essto y como puedo hcer que se pinte en la matriz del inicio

def __init__(self, grid_state):
    self.grid_state = grid_state
    self.matriz_bridges = [[' ' for _ in range(len(grid_state[0]))] for _ in range(len(grid_state))]
    self.actualizar_matriz()

def actualizar_matriz(self):
    """Convierte el estado del grid a una matriz de puentes."""
    for i, fila in enumerate(self.grid_state):
        fila_str = ''.join(cell.get() if cell.get() != "" else ' ' for cell in fila)
        for j in range(len(fila_str)):
            self.matriz_bridges[i][j] = fila_str[j]

def resolver(self):
    """Intenta resolver el juego aplicando una estrategia."""
    while True:
        progreso = self.realizar_movimiento()
        self.actualizar_matriz()

        # Verifica si el jugador ganó
        matriz_valida = Bridges.validar_matriz(self.matriz_bridges)
        solucion = Bridges.validar_conexiones_necesarias(self.matriz_bridges)
        ganador = Bridges.validar_solucion(solucion)

        if ganador and matriz_valida and Bridges.generar_grafo(self.matriz_bridges):
            print("¡GANÓ EL JUGADOR SINTÉTICO!")
            return True

        if not progreso:
            print("El jugador sintético se quedó sin movimientos válidos.")
            return False

def realizar_movimiento(self):
    """Realiza un movimiento basado en la heurística."""
    for i in range(len(self.matriz_bridges)):
        for j in range(len(self.matriz_bridges[i])):
            if self.es_isla(i, j):
                conexiones_restantes = self.conexiones_necesarias(i, j)
                if conexiones_restantes > 0:
                    if self.conectar_isla(i, j):
                        return True  # Se hizo progreso
    return False  # No se pudo hacer progreso

def es_isla(self, i, j):
    """Verifica si la celda actual es una isla."""
    return self.matriz_bridges[i][j].isdigit()

def conexiones_necesarias(self, i, j):
    """Calcula cuántas conexiones faltan para una isla."""
    conexiones_actuales = sum(self.contar_conexiones(i, j, d) for d in ["N", "S", "E", "O"])
    return int(self.matriz_bridges[i][j]) - conexiones_actuales

def contar_conexiones(self, i, j, direccion):
    """Cuenta las conexiones en una dirección específica."""
    # Implementar lógica para contar conexiones en cada dirección (Norte, Sur, Este, Oeste)
    # Por ejemplo:
    if direccion == "N":  # Norte
        for x in range(i - 1, -1, -1):
            if self.es_isla(x, j):
                return 1  # Hay un puente
    # Implementar lógica para las otras direcciones...
    return 0

def conectar_isla(self, i, j):
    """Intenta conectar la isla actual con otra cercana."""
    direcciones = ["N", "S", "E", "O"]
    for d in direcciones:
        if self.puede_conectar(i, j, d):
            self.poner_puente(i, j, d)
            return True
    return False

def puede_conectar(self, i, j, direccion):
    if direccion == "E":  # Este
        for y in range(j + 1, len(self.matriz_bridges[0])):
            if self.matriz_bridges[i][y].isdigit():  # Encuentra otra isla
                return True
            elif self.matriz_bridges[i][y] not in ['-', '=', ' ']:  # Obstáculo
                break
    # Implementar lógica para N, S, O
    return False

def poner_puente(self, i, j, direccion):
    if direccion == "E":
        for y in range(j + 1, len(self.matriz_bridges[0])):
            if self.matriz_bridges[i][y].isdigit():  # Encuentra otra isla
                break
            self.matriz_bridges[i][y] = '-' if self.matriz_bridges[i][y] == ' ' else '='

