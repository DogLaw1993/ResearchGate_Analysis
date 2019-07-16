from co_author_crawler import crawler
import graph

if __name__ == '__main__':
    nodes1 = []
    nodes2 = []
    edges = []

    graph.get_graph(nodes1, nodes2, edges)
    graph.get_graph_by_institution(nodes1, nodes2, edges)
