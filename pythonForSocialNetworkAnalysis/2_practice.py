%matplotlib notebook
import networkx as nx
import matplotlib.pyplot as plt
from networkx import layout


# read in the graph
G = nx.path_graph(4)
nx.write_gpickle(G, "major_us_cities")
G = nx.read_gpickle('major_us_cities')

# draw the graph using the default spring layout
# plt.figure(figsize=(10,9))
nx.draw_networkx(G)

ee what layouts are available in networkX
[x for x in layout.__all__ if x.endswith('_layout')]

# Draw the graph using the random layout
# plt.figure(figsize=(10,9))
pos = nx.random_layout(G)
nx.draw_networkx(G, pos)

# Draw the graph using the circular layout
# plt.figure(figsize=(10,9))
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos)

# Draw the graph adding alpha, removing labels, and softening edge color
# plt.figure(figsize=(10,7))
pos = nx.random_layout(G)
nx.draw_networkx(G, pos, alpha=0.7, with_labels=False, edge_color='.4')
plt.axis('off')
plt.tight_layout();
