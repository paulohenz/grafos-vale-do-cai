class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}

    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)
        self.arestas[vertice] = []

    def adicionar_aresta(self, origem, destino, peso):
        self.arestas[origem].append((destino, peso))
        self.arestas[destino].append((origem, peso))

    def dijkstra(self, origem, destino):
        distancias = {vertice: float('infinity') for vertice in self.vertices}
        distancias[origem] = 0
        visitados = set()

        while visitados != self.vertices:
            atual = min((vertice for vertice in self.vertices if vertice not in visitados), key=lambda vertice: distancias[vertice])
            visitados.add(atual)

            for vizinho, peso in self.arestas[atual]:
                nova_distancia = distancias[atual] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia

        caminho = []
        atual = destino
        while atual != origem:
            caminho.insert(0, atual)
            atual = min((vertice for vertice in self.vertices if vertice in [vizinho for vizinho, _ in self.arestas[atual]]), key=lambda vertice: distancias[vertice])

        caminho.insert(0, origem)
        return caminho, distancias[destino]


# Exemplo de uso
grafo = Grafo()

# Adiciona vértices
grafo.adicionar_vertice("Feliz")
grafo.adicionar_vertice("Vale Real")
grafo.adicionar_vertice("Alto Feliz")
grafo.adicionar_vertice("Bom Princípio")
grafo.adicionar_vertice("Tupandi")
grafo.adicionar_vertice("São Vendelino")
grafo.adicionar_vertice("S.S. do Caí")

# Adiciona arestas
grafo.adicionar_aresta("Feliz", "Vale Real", 10.2)
grafo.adicionar_aresta("Feliz", "Bom Princípio", 8.0)
grafo.adicionar_aresta("Feliz", "Alto Feliz", 11.3)
grafo.adicionar_aresta("Feliz", "S.S. do Caí", 22.5)
grafo.adicionar_aresta("Bom Princípio", "São Vendelino", 17.9)
grafo.adicionar_aresta("Bom Princípio", "S.S. do Caí", 12.6)
grafo.adicionar_aresta("Bom Princípio", "Tupandi", 10.8)
grafo.adicionar_aresta("S.S. do Caí", "Tupandi", 18.0)
grafo.adicionar_aresta("São Vendelino", "Alto Feliz", 11.1)

# Encontra o menor caminho
caminho, distancia = grafo.dijkstra("Feliz", "Alto Feliz")
print(f"Menor caminho: {caminho}")
print(f"Distância: {distancia}")