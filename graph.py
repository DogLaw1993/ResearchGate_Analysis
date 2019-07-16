import networkx as nx
import matplotlib.pyplot as plt

def get_graph(names1,names2,edges):
    G=nx.Graph()
    G.add_nodes_from(names1)
    G.add_nodes_from(names2)
    G.add_edges_from(edges)

    nx.draw(G)
    plt.show()

def get_graph_by_institution(names1,names2,edges):
    G = nx.Graph()
    G.add_nodes_from(names1)
    G.add_nodes_from(names2)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(names1, pos, node_color='r')
    nx.draw_networkx_nodes(names2, pos, node_color='g')
    nx.draw_networkx_edges(G, pos)
    plt.show()