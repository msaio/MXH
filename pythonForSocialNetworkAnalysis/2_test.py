import networkx as nx
import numpy as np
import pandas as pd
%matplotlib notebook

# Question 1
# Using networkx, load up the directed multigraph from email_network.txt. Make sure the node names are strings.
# This function should return a directed multigraph networkx graph.
def answer_one():
    G = nx.read_edgelist('email_network.txt', delimiter='\t', data=[('timestamp', int)], create_using=nx.MultiDiGraph())
    return G

# x = answer_one()
# x


# Question 2
# How many employees and emails are represented in the graph from Question 1?
# This function should return a tuple (#employees, #emails).
def answer_two():
    G = answer_one()
    return len(G.nodes()), len(G.edges())

# x = answer_two()
# x


# Question 3
# * Part 1. Assume that information in this company can only be exchanged through email.
# When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but not vice versa.
# Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?

# * Part 2. Now assume that a communication channel established by an email allows information to be exchanged both ways.
# Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?

# This function should return a tuple of bools (part1, part2).
def answer_three():    
    G = answer_one()
    return nx.is_strongly_connected(G), nx.is_connected(G.to_undirected())

# x = answer_three()
# x


# Question 4
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# This function should return an int.
def answer_four():
    G = answer_one()
    wccs = nx.weakly_connected_components(G)
    return len(max(wccs, key=len))

# x = answer_four()
# x


# Question 5
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# This function should return an int
def answer_five():
    G = answer_one()
    sccs = nx.strongly_connected_components(G)
    return len(max(sccs, key=len))

# x = answer_five()
# x


# Question 6
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of nodes in a largest strongly connected component. Call this graph G_sc.
# This function should return a networkx MultiDiGraph named G_sc.
def answer_six():
    G = answer_one()
    scc_subs = nx.strongly_connected_component_subgraphs(G)
    G_sc = max(scc_subs, key=len)
    return G_sc

# x = answer_six()
# x.edges()


# Question 7
# What is the average distance between nodes in G_sc?
# This function should return a float.
def answer_seven():
    G = answer_six()
    return nx.average_shortest_path_length(G)

# x = answer_seven()
# x 


# Question 8
# What is the largest possible distance between two employees in G_sc?
# This function should return an int.
def answer_eight():
    G = answer_six()
    return nx.diameter(G)

# x = answer_eight()
# x


# Question 9
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# This function should return a set of the node(s).
def answer_nine():
    G = answer_six()
    return set(nx.periphery(G))

# x = answer_nine()
# x


# Question 10
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# This function should return a set of the node(s).
def answer_ten():
    G = answer_six()
    return set(nx.center(G))

# x = answer_ten()
# x


# Question 11
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc?
# How many nodes are connected to this node?
# This function should return a tuple (name of node, number of satisfied connected nodes).
def answer_eleven():
    G = answer_six()
    d = nx.diameter(G)
    peripheries = nx.periphery(G)
    max_count = -1
    result_node = None
    for node in peripheries:
        sp = nx.shortest_path_length(G, node)
        count = list(sp.values()).count(d)
        if count > max_count:
            result_node = node
            max_count = count
            return result_node, max_count

# x = answer_eleven()
# x


# Question 12
# Suppose you want to prevent communication from flowing to the node that you found in the previous question from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or the center nodes)?
# This function should return an integer.
def answer_twelve():
    G = answer_six()
    center = nx.center(G)[0]
    node = answer_eleven()[0]
    return len(nx.minimum_node_cut(G, center, node))

# x = answer_twelve()
# x


# Question 13
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# This function should return a networkx Graph.
def answer_thirteen():
    G = answer_six()
    undir_subgraph = G.to_undirected()
    G_un = nx.Graph(undir_subgraph)
    return G_un

# x = answer_thirteen()
# x.edges()
# x


# Question 14
# What is the transitivity and average clustering coefficient of graph G_un?
# This function should return a tuple (transitivity, avg clustering).
def answer_fourteen():
    G = answer_thirteen()
    return nx.transitivity(G), nx.average_clustering(G)

# x = answer_fourteen()
# x 
