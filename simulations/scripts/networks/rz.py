import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import cmath

gamma = 0.5 + 1.5j
pd1 = [cmath.polar(k ** gamma)[0] for k in range(1, 25)]
pd2 = [cmath.polar(k ** gamma)[1] for k in range(1, 25)]

print(pd1)
print(pd2)
#pd=[x ** 0.5 for x in range(1, 85)]
#pd2=[x ** 0.5 for x in range(1, 75)]
G1=nx.expected_degree_graph(pd1, selfloops=False)
G2=nx.expected_degree_graph(pd2, selfloops=False)
nx.draw(G1, node_color="green")
nx.draw(G2)
plt.show()
