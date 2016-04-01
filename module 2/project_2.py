"""
Project 2: bfs_visited
"""
from collections import deque

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def bfs_visited(ugraph, start_node):
    """
    bfs_visited, return a list of visited nodes
    """
    queque = deque()
    start = start_node
    graph = copy_graph(ugraph)

    queque.append(start)
    visited = set()
    visited.add(start)

    while (queque):
        deq = queque.popleft()
        if deq in graph:
            for neighbor in graph[deq]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queque.append(neighbor)

    return visited

# print bfs_visited(g, 1)

def cc_visited(ugraph):
    """
    cc_visited, return a list of sets, each are connected nodes
    """
    remain = []
    graph = copy_graph(ugraph)
    for each in graph:
        remain.append(each)

    cc_list = []
    while len(remain):
        cluster = bfs_visited(graph, remain.pop())
        cc_list.append(cluster)

        for each in cluster:
            if each in remain:
                remain.remove(each)

    return cc_list

#print cc_visited(h)

def largest_cc_size(ugraph):
    """
    largest_CC_size, return size of largest cc_visited set
    """
    maxn = 1
    graph = copy_graph(ugraph)
    cc_list = cc_visited(graph)

    if cc_list:
        for each in cc_list:
            if len(each) > maxn:
                maxn = len(each)

    if not graph:
        return 0
    else:
        return maxn

#print largest_cc_size(g)

def compute_resilience(ugraph, attack_order):
    """
    return: len(largest_cc), len(largest_cc after removal 1st node), len(largest_cc after removal 1st and 2nd node)...
    """
    graph = copy_graph(ugraph)
    cc_len = []
    cc_len.append(largest_cc_size(graph))

    attack_list= deque()
    for each in attack_order:
        attack_list.append(each)

    while (attack_list):
        node = attack_list.popleft()

        if node in graph:
            del graph[node]

        for each in graph:
            if node in graph[each]:
                graph[each].remove(node)

        #print graph
        cc_len.append(largest_cc_size(graph))

    return cc_len
