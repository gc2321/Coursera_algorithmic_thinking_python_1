# -*- coding: utf-8 -*-
"""
Application Q2
"""
import random

# generate directed ER graph

graph = {}
nodes = list(range(0,1000))
for each in nodes:
    graph[each] = set()
    for item in nodes:
        if each !=item and random.randint(0,3)==1:
            graph[each].add(item)

# print graph

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph and computes the in-degrees
    for the nodes in the graph.
    ie. in digraph, for each node, obtain the number nodes from which it receives an edge head
    """
    graph = {}
    for each in digraph:
        graph[each] = 0

    for each in digraph:
        for value in digraph[each]:
            graph[value] +=1

    return graph

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph and computes the unnormalized
    distribution of the in-degrees of the graph.
    eg. in digraph, compute {in_degree number: number of node with that in_degree}
    """
    dist = {}
    deg_dic = compute_in_degrees(digraph)
    for each in deg_dic:
        if deg_dic[each] in dist:
            dist[deg_dic[each]] +=1
        else:
            dist[deg_dic[each]] =1

    return dist

def normalized_distribution(digraph):
    total = 0
    dist = {}
    for each in digraph:
        total += digraph[each]
    for each in digraph:
        dist[each] = (digraph[each]*1.0)/total

    return dist


citation_dic = in_degree_distribution(graph)

# create a normalized in-degree distribution

norm_indegree = normalized_distribution(citation_dic)

#print norm_indegree

# generate plot

import matplotlib.pyplot as plt
import math

for key, value in norm_indegree.items():
   x = key
   y = value
   plt.scatter(x,y)

#plt.legend(norm_indegree.keys())
#plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1, 1000)
plt.title('Normalized in-degree distribution of ER graph with p=0.25')
plt.ylabel('In-degree distribution (normalized)')
plt.xlabel('Number of nodes')
plt.show()


