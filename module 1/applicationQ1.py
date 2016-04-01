# -*- coding: utf-8 -*-
"""
Application Q1
"""
import urllib2

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

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
    
       
citation_graph = load_graph(CITATION_URL)
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
plt.title('Normalized in-degree distribution of citation \n in high energy physics theory papers\n')
plt.ylabel('Distribution of citation (normalized)')
plt.xlabel('Number of papers')
plt.show()








