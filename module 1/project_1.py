# -*- coding: utf-8 -*-
"""
Project 1 - Degree distributions for graphs 

"""
EX_GRAPH0 = { 
    0: set([1,2]),
    1: set(),
    2: set()
}

EX_GRAPH1 = { 
    0: set([1,4,5]),
    1: set([2,6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set()
}

EX_GRAPH2 = { 
    0: set([1,4,5]),
    1: set([2,6]),
    2: set([3,7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set(),
    7: set([3]),
    8: set([1,2]),
    9: set([0,3,4,5,6,7])
}

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary 
    corresponding to a complete directed graph with the specified
    number of nodes.
    
    """
    graph = {}
    for node1 in range(num_nodes):
        node_set = set()
        for node2 in range(num_nodes):          
            if node1 != node2:
                node_set.add(node2)           
        graph [node1] = node_set   
    return graph

# print make_complete_graph(5)

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

#print compute_in_degrees(EX_GRAPH0)

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
    
#print in_degree_distribution(EX_GRAPH0)
    
    
    
    
    
    
    
    

