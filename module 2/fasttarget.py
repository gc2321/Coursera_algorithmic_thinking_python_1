# Q3

#g = {0: set([]), 1: set([2]), 2: set([1]), 3: set([4]), 4: set([3])}
#h = {23: set([]), 11: set([2]), 222: set([1]), 83: set([4]), 40: set([3])}

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def fast_target_order(ugraph):
    """
    find in ugraph a list of nodes with decreasing number of degree
    :param ugraph:
    :return: node list
    """
    node_list =[]
    deg_set ={}

    graph = copy_graph(ugraph)

    for i in range(0, len(graph)):
        deg_set[i] = set()

    for key, value in graph.items():
        # degree at each node
        deg = len(value)
        # add node to deg_set according to degree of this node
        deg_set[deg].add(key)

    #count = 0

    for i in range ((len(graph)-1),-1, -1):
        while deg_set[i]:
            # each = u
            each = deg_set[i].pop()
            if len(graph[each]):
                #print each
                for neighbor in graph[each]:
                    #print neighbor
                    #print graph[neighbor]
                    #print len(graph[neighbor])
                    if neighbor in graph:
                        d = len(graph[neighbor])
                        if neighbor in deg_set[d]:
                            deg_set[d].remove(neighbor)
                            deg_set[d-1].add(neighbor)

            node_list.append(each)

            #count +=1
            del graph[each]

    return node_list

#print fast_target_order(g)
