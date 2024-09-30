class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 not in self.grafo:
            self.agregar_nodo(nodo1)
        if nodo2 not in self.grafo:
            self.agregar_nodo(nodo2)
        # Como es no dirigido, agregar en ambos sentidos
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)

    def mostrar_grafo(self):
        for nodo, vecinos in self.grafo.items():
            print(f"{nodo}: {', '.join(vecinos)}")

    def es_conexo(self):
        if not self.grafo:
            return True  # Si el grafo está vacío, lo consideramos conexo

        # Escoger un nodo inicial arbitrario
        nodo_inicial = next(iter(self.grafo))

        # Realizar un recorrido DFS para visitar todos los nodos
        visitados = set()
        self.dfs(nodo_inicial, visitados)

        # Verificar si todos los nodos han sido visitados
        return len(visitados) == len(self.grafo)

    def dfs(self, nodo, visitados):
        visitados.add(nodo)
        for vecino in self.grafo[nodo]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)