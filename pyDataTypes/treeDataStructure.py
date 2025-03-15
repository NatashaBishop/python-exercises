# Tree data structure is a hierarchical structure that is used to represent and organize data in the form of parent child relationship
# In computer science, a tree is a non-linear data structure consisting of nodes connected by edges. 
# It comprises a root node, which serves as the starting point, and each node can have zero or more child nodes.
#example of building a tree:

import networkx as nx #The library enables each node to be any hashable object, and there is no constraint on the number of children each node has.
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('A', 'E')
G.add_edge('E', 'F')

# Create tree from list, print tree
from bigtree import list_to_tree #, tree_to_dict, tree_to_dot
root = list_to_tree(["a/b/d", "a/c"])
print_tree(root)
# a
# ├── b
# │   └── d
# └── c

# example with treelib
from treelib import Node, Tree
tree = Tree() # creating an object
tree.create_node("Harry", "harry")  # root node 
tree.create_node("Jane", "jane", parent="harry") #adding nodes
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()
'''
Harry
├── Bill
└── Jane
    ├── Diane
    │   └── Mary
    └── Mark
'''
