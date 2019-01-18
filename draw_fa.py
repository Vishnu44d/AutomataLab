import networkx as nx
from automata import nfa, dfa
import matplotlib.pyplot as plt

def draw(fa):
    G = nx.MultiDiGraph()
    for s in fa:
        for symbol in fa[s]:
            ns = fa[s][symbol]
            for e in ns:
                G.add_edge(s, e, weight = symbol)
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == '0']
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == '1']
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=elarge,width=6, edge_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=esmall,width=6, alpha=0.5, edge_color='b')
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    plt.axis('off')
    plt.show()

draw(nfa)