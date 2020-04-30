import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(2,3)
pos=nx.shell_layout(G)
#G.add_edge(1, 2 )
#G.add_edges_from([(3, 4), (4, 5),(3,5)], color='red')
#G.add_edges_from([(1, 2, {'color': 'red'}), (2, 3, {'color':'green'})])

#nx.draw(G)
#nx.draw_networkx_edge_labels(G,{1:[100,200],2:[2,3],3:[3,4],4:[4,5],5:[6,7]},edge_labels={(3,4):"666"})
print(G.edges(data=True))
nx.draw(G,pos)
nx.draw_networkx_edge_labels(G,pos=pos, edge_labels = {(2,3):"666"},font_size=8)
plt.show()