import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


#1
# G = nx.Graph()
     #or
# G = nx.DiGraph()
        #or
# G = nx.MultiGraph()
       #or
# G = nx.MultiDiGraph()
       #or
# G.add_edge(1,2)
# G.add_edge(2,3,weight=0.9)
# G.add_edge("A","B")
# G.add_edge("B","B")
# G.add_node("C")
# G.add_node(print)

# nx.draw_spring(G,with_labels=True)
# plt.show()


#2
# edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7)]
# G = nx.Graph()
# G.add_edges_from(edge_list)
#
# print(nx.adjacency_matrix(G))

#3
# G = nx.from_numpy_array(np.array([[0,1,0],
#          [1,1,1],
#          [0,0,0]]))
#
# nx.draw_spring(G,with_labels=True)
#
# nx.draw_circular(G,with_labels=True)

#4 centrality
edge_list = [(1,2),(2,3),(3,4),(3,5),(4,6),(6,7),(2,8),(8,9),(9,4)]
G1 = nx.complete_graph(5)
G2 = nx.complete_graph(5)
G2 = nx.relabel_nodes(G2,{0:"A",1:"B",2:"C",3:"D",4:"E"})
G_connector = nx.from_edgelist([(4,"X"),("X","A")])

G = nx.compose_all([G1,G2,G_connector])
print(nx.degree_centrality(G))
print(nx.betweenness_centrality(G))

print(nx.density(G))
print(nx.diameter(G))
nx.draw_spring(G,with_labels=True)

plt.show()
print(list(nx.eulerian_path(G) ))
print(list(nx.find_cliques(G)))
#official documentation
#https://networkx.org/documentation/stable/tutorial.html
