#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:46:09 2019

@author: sanjeevkumar
"""

import os
#import fileIO
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community
import graphviz
from itertools import chain
from networkx.drawing.nx_agraph import graphviz_layout

list_of_users = pd.read_csv('/Users/sanjeevkumar/Desktop/ML/community_data.csv', header=None )
list_of_users.head()
G = nx.Graph()

for item in list_of_users.itertuples():
    source = item[3]
    destination = item[2]
    weight = item[1]
    id_elem = item[0]
    G.add_node(int(source))
    G.add_node(int(destination))
    G.add_edge(int(source), int(destination), weight=int(weight))

nx.draw_spring(G)
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

edge_colors = 'red'
pos=nx.spring_layout(G)
nx.draw(G, pos, width=1.5, alpha=0.5)
plt.savefig("First_Graph.png")
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.5)


partition = community.best_partition(G)

print( len(partition))

partition_set = set()
for item in partition.values():
    partition_set.add(item)

induced_graph = community.induced_graph(partition, G)
print (induced_graph.edges(data='weight'))

pos=nx.spring_layout(induced_graph)
nx.draw(induced_graph, pos, width=0.5, alpha=0.5)
plt.savefig("Induced_Graph.png")
nx.draw_networkx_edges(induced_graph, pos, width=0.5, alpha=0.5)


cluster_size = []
for i in range(168):
    cluster_size.append(0)


for key, value in partition.items(): 
    cluster_size[value] += 1
    print (key, value)

if not os.path.exists("output"):
    os.makedirs("output")

#write_file("output/output.csv", partition)
#write_induced_graph("output/induced_graph.csv", induced_graph.edges(data='weight'))
#write_number_of_nodes('output/number_of_nodes.csv', cluster_size)

modularity = community.modularity(partition, G, weight='weight')
print ("Modularity = ", modularity)
