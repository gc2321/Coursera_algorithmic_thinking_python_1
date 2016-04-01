
import random
import provided as provided
import alg_upa_trial as alg
import project_2 as p2
import matplotlib.pyplot as plt
import timeit
import fasttarget as fast

# network_graph = provided.load_graph(provided.NETWORK_URL)
# print "\n"

# generate undirected ER graph

def ER_Graph(node, p):
    """
    :param node: number of nodes in graph
    :param prob: probability of an edge if formed, if prob =2, prob=1/3 (0,1,2)
    :return: graph
    """

    graph = {}
    nodes = list(range(0,node))
    while (nodes):

        popnode = nodes[0]
        if popnode not in graph:
            graph[popnode] = set()

        for each in nodes:
            if each!=popnode and random.randint(0,p)==0:
                graph[popnode].add(each)
                if each in graph:
                    graph[each].add(popnode)
                else:
                    graph[each] = set()
                    graph[each].add(popnode)

        nodes.pop(0)

    return graph

#print ER_Graph(5)

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary
    corresponding to a complete undirected graph with the specified
    number of nodes.

    """
    graph = {}
    upa = alg.UPATrial(num_nodes)

    for i in range(num_nodes):
        if i not in graph:
            graph[i] = set()

        neighbors = upa.run_trial(num_nodes)
        #print neighbors

        for each in neighbors:
            if each!=i:
                graph[i].add(each)

            if (each in graph) and (each!=i):
                graph[each].add(i)
            elif (each!=i):
                graph[each] = set()
                graph[each].add(i)

    return graph

#print make_complete_graph(4)

def out_degree(digraph):
    """
    determine the average number of out-degree for undirected graph
    :param digraph: undirected graph
    :return: total number of nodes, and average number of edges
    """
    node = 0
    out_degree = 0
    for each in digraph:
        node +=1
        out_degree += len(digraph[each])

    #out_degree = out_degree*1.0
    print "Total number of nodes is "+str(node)
    print "Average number of neighbors per node "+str((out_degree*1.0)/node)
    print "Average number of undirected edges is "+str((out_degree*0.5)/node)

def upa_graph(n,m):

    # step 1: make a complete graph with m nodes
    graph_dic = make_complete_graph(m)

    graph = alg.UPATrial(m)

    # step 2: add to graph from m to n nodes, one node per iteration
    # for each iteration, add m out-degree to each new node

    for i in range(m, n):
        if i not in graph_dic:
            graph_dic[i] = set()

        number = random.randint(m, m+1)
        neighbors = graph.run_trial(number)
        #print neighbors

        for each in neighbors:
            if each!=i:
                graph_dic[i].add(each)

            if (each in graph_dic) and (each!=i):
                graph_dic[each].add(i)
            elif (each!=i):
                graph_dic[each] = set()
                graph_dic[each].add(i)

    return graph_dic

def random_order(graph):
    """
    generate list of random nodes using all the nodes in the graph
    return: list of random nodes
    """
    nodes=[]
    for each in graph:
        nodes.append(each)

    list=[]
    while len(nodes):
        choice = random.choice(nodes)
        list.append(choice)
        nodes.remove(choice)

    return list

#test = ER_Graph(4,0)
#print test
#print random_order(test)

#print "Network graph:"
#out_degree(network_graph)
#network_node_list = p2.compute_resilience(network_graph, random_order(network_graph))
#print "\n"

# generate ER graph
#print "ER graph:"
#ERgraph = ER_Graph(1239, 248)
#out_degree(ERgraph)
#er_node_list = p2.compute_resilience(ERgraph, random_order(ERgraph))
#print "\n"

# generate UPA graph
#print "UPA graph:"
#UPAgraph = upa_graph(1239,2)
#out_degree(UPAgraph)
#upa_node_list = p2.compute_resilience(UPAgraph, random_order(UPAgraph))
#print "\n"

# Q1
# plot graph
# x = list(range(1240))
# plt.plot(x,network_node_list)
# plt.plot(x,er_node_list)
# plt.plot(x,upa_node_list)
# plt.legend(['Network graph', 'ER graph (p=0.004)', 'UPA graph(m=2)'], loc='upper right')
# plt.title('Resilience of Network graph, ER graph, and UPA graph')
# plt.ylabel('Size of the largest connect component')
# plt.xlabel('Number of nodes removed')
#
# plt.show()

#Q3
n= list(range(10, 1000, 10))
time_fast=[]
time_random=[]

for each in n:
    UPAgraph = upa_graph(each,5)

    start1 = timeit.default_timer()
    #fast_node_list = p2.compute_resilience(UPAgraph, fast.fast_target_order(UPAgraph))
    fast.fast_target_order(UPAgraph)
    stop1 = timeit.default_timer() - start1

    time_fast.append(stop1)

    start2 = timeit.default_timer()
    #random_node_list = p2.compute_resilience(UPAgraph, provided.targeted_order(UPAgraph))
    provided.targeted_order(UPAgraph)
    stop2 = timeit.default_timer() - start2

    time_random.append(stop2)

#print time_fast
#print time_random

#plot graph

plt.plot(n,time_fast)
plt.plot(n,time_random)
plt.legend(['FastTargetOrder', 'TargetOrder'], loc='upper left')
plt.title('Comparing efficiency of FastTargetOrder and TargetOrder \n on finding attack order list of UPA graph (m=5) using desktop Python ')
plt.ylabel('Time (s)')
plt.xlabel('Number of nodes')

plt.show()







# Q4
# network_node_list = p2.compute_resilience(network_graph, provided.targeted_order(network_graph))
# er_node_list = p2.compute_resilience(ERgraph, provided.targeted_order(ERgraph))
# upa_node_list = p2.compute_resilience(UPAgraph, provided.targeted_order(UPAgraph))

#plot graph
# x = list(range(1240))
# plt.plot(x,network_node_list)
# plt.plot(x,er_node_list)
# plt.plot(x,upa_node_list)
# plt.legend(['Network graph', 'ER graph (p=0.004)', 'UPA graph(m=2)'], loc='upper right')
# plt.title('Resilience of Network graph, ER graph, and UPA graph \n using targeted_order()')
# plt.ylabel('Size of the largest connect component')
# plt.xlabel('Number of nodes removed')
#
# plt.show()
