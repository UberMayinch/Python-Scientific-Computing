
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import cmath

gamma = 0.5 + 1.5j
pd1 = [cmath.polar(k ** gamma)[0] for k in range(1, 25)]
pd2 = [cmath.polar(k ** gamma)[1] for k in range(1, 25)]

# Create a directed graph where negative expected degrees represent the difference between outdegree and indegree
G1 = nx.directed_configuration_model(pd1, pd2)
G2 = nx.directed_configuration_model(pd2, pd1)

nx.draw(G1, node_color="green", with_labels=True)
nx.draw(G2, with_labels=True)
plt.show()
