# -*- coding: utf-8 -*-
"""
Application Q3
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

citation_graph = load_graph(CITATION_URL)

#print citation_graph[9912246]

def out_degree(digraph):
    node = 0
    out_degree = 0
    for each in digraph:
        node +=1
        out_degree += len(digraph[each])

    #out_degree = out_degree*1.0
    print "Total number of nodes is "+str(node)
    print "Average number of out-degree is "+str(out_degree/(node*1.0))

out_degree(citation_graph)