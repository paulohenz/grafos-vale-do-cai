class Grafo {
    constructor() {
        this.vertices = new Set();
        this.arestas = {};
    }

    adicionarVertice(vertice) {
        this.vertices.add(vertice);
        this.arestas[vertice] = [];
    }

    adicionarAresta(origem, destino, peso) {
        this.arestas[origem].push({ destino, peso });
        this.arestas[destino].push({ origem, peso });
    }

    dijkstra(origem, destino) {
        const distancias = {};
        const visitados = new Set();

        for (const vertice of this.vertices) {
            distancias[vertice] = Infinity;
        }

        distancias[origem] = 0;

        while (visitados.size !== this.vertices.size) {
            const atual = Array.from(this.vertices).filter(vertice => !visitados.has(vertice)).reduce((min, vertice) => distancias[vertice] < distancias[min] ? vertice : min, origem);

            visitados.add(atual);

            for (const { vizinho, peso } of this.arestas[atual]) {
                const novaDistancia = distancias[atual] + peso;

                if (novaDistancia < distancias[vizinho]) {
                    distancias[vizinho] = novaDistancia;
                }
            }
        }

        const caminho = [];
        let atual = destino;

        while (atual !== origem) {
            caminho.unshift(atual);
            atual = Array.from(this.vertices).filter(vertice => this.arestas[atual].some(v => v.vizinho === vertice)).reduce((min, vertice) => distancias[vertice] < distancias[min] ? vertice : min, origem);
        }

        caminho.unshift(origem);

        return { caminho, distancia: distancias[destino] };
    }
}

// Criação do grafo e adição de vértices e arestas
const grafo = new Grafo();

grafo.adicionarVertice("Feliz");
grafo.adicionarVertice("Vale Real");
grafo.adicionarVertice("Alto Feliz");
grafo.adicionarVertice("Bom Princípio");
grafo.adicionarVertice("Tupandi");
grafo.adicionarVertice("São Vendelino");
grafo.adicionarVertice("S.S. do Caí");

grafo.adicionarAresta("Feliz", "Vale Real", 10.2);
grafo.adicionarAresta("Feliz", "Bom Princípio", 8.0);
grafo.adicionarAresta("Feliz", "Alto Feliz", 11.3);
grafo.adicionarAresta("Feliz", "S.S. do Caí", 22.5);
grafo.adicionarAresta("Bom Princípio", "São Vendelino", 17.9);
grafo.adicionarAresta("Bom Princípio", "S.S. do Caí", 12.6);
grafo.adicionarAresta("Bom Princípio", "Tupandi", 10.8);
grafo.adicionarAresta("S.S. do Caí", "Tupandi", 18.0);
grafo.adicionarAresta("São Vendelino", "Alto Feliz", 11.1);

// Exporta a classe Grafo para ser usada em outros arquivos
export default Grafo;

// Função para encontrar o menor caminho
window.encontrarMenorCaminho = function (origem, destino) {
    const { caminho, distancia } = grafo.dijkstra(origem, destino);
    const resultadoElement = document.getElementById("resultado");
    resultadoElement.innerHTML = `Menor caminho: ${caminho.join(" -> ")} <br> Distância: ${distancia}`;
};
