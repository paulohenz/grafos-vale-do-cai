from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'


# Criar um objeto grafo
grafo = Digraph('MeuGrafo')

# Adicionar nós e arestas ao grafo
grafo.edge("Feliz", "Vale Real")
grafo.edge("Feliz", "Bom Princípio")
grafo.edge("Feliz", "Alto Feliz")
grafo.edge("Feliz", "S.S. do Caí")
grafo.edge("Bom Princípio", "São Vendelino")
grafo.edge("Bom Princípio", "S.S. do Caí")
grafo.edge("Bom Princípio", "Tupandi")
grafo.edge("S.S. do Caí", "Tupandi")
grafo.edge("São Vendelino", "Alto Feliz")

# Salvar o grafo como imagem
grafo.render('grafo', format='png', cleanup=True)

print("Grafo gerado com sucesso!")
