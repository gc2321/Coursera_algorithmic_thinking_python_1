# -*- coding: utf-8 -*-
"""
Application Q4
"""

import random
import alg_dpa_trial as alg

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary
    corresponding to a complete directed graph with the specified
    number of nodes.

    """
    graph = {}
    dpa = alg.DPATrial(num_nodes)

    for i in range(num_nodes):
        graph[i]= dpa.run_trial(num_nodes)

    return graph

#print make_complete_graph(15)

def dpa_graph(n,m):

    # step 1: make a complete graph with m nodes
    graph_dic = make_complete_graph(m)

    graph = alg.DPATrial(m)

    # step 2: add to graph from m to n nodes, one node per iteration
    # for each iteration, add m out-degree to each new node

    for i in range(m, n):
        graph_dic[i] = graph.run_trial(m)

    return graph_dic

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


#print dpa_graph(100, 13)

citation_graph = dpa_graph(27770, 13)
citation_dic = in_degree_distribution(citation_graph)

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
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1, 1000)
plt.title('Normalized in-degree distribution of DPA graph\n')
plt.ylabel('Distribution of in-degree (normalized)')
plt.xlabel('Number of nodes')
plt.show()

