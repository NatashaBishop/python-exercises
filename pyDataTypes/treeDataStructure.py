# Tree data structure is a hierarchical structure that is used to represent and organize data in the form of parent child relationship
# In computer science, a tree is a non-linear data structure consisting of nodes connected by edges. It comprises a root node, which serves as the starting point, and each node can have zero or more child nodes.
#example of building a tree:

import networkx as nx #The library enables each node to be any hashable object, and there is no constraint on the number of children each node has.
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('A', 'E')
G.add_edge('E', 'F')

