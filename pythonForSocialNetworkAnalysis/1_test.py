import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite


# This is the set of employees
employees = set(['Pablo',
                 'Lee',
                 'Georgia',
                 'Vincent',
                 'Andy',
                 'Frida',
                 'Joan',
                 'Claude'])

# This is the set of movies
movies = set(['The Shawshank Redemption',
              'Forrest Gump',
              'The Matrix',
              'Anaconda',
              'The Social Network',
              'The Godfather',
              'Monty Python and the Holy Grail',
              'Snakes on a Plane',
              'Kung Fu Panda',
              'The Dark Knight',
              'Mean Girls'])


# you can use the following function to plot graphs
# make sure to comment it out before submitting to the autograder
def plot_graph(G, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    %matplotlib notebook
    import matplotlib.pyplot as plt
    
    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None
    
    if weight_name:
        weights = [int(G[u][v][weight_name]) for u,v in edges]
        labels = nx.get_edge_attributes(G,weight_name)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights);
    else:
        nx.draw_networkx(G, pos, edges=edges);


# Load in the bipartite from Employee_Movie_Choices.txt and return that graph.
def answer_one():        
    movie_choices = nx.read_edgelist('Employee_Movie_Choices.txt', delimiter="\t") 
    return movie_choices

# plot_graph(answer_one())


# Using the graph from the previous question, add nodes attributes named 'type' where movies have the value 'movie' and employees have the value 'employee' and return that graph
# This function should return a networkx graph with node attributes {'type' : 'movie'} or {'type':'employee'}
def answer_two():
    B = answer_one()
    for node in B.nodes():
        if node in employees:
            B.add_node(node, type="employee")
        else:
            B.add_node(node, type="movie")
    return B

# answer_two()


#Find a weighted projection of the graph from answer_two which tells us how many movies different pairs of employees have in common
#This function should return a weighted projected graph
def answer_three():
    B = answer_two()
    weighted_proj = bipartite.weighted_projected_graph(B, employees)
    return weighted_proj

# answer_three()


# Suppose you'd like to find out if people that have a high relationship score also like the same types of movies.
# Find the Pearson correlation ( using DataFrame.corr() ) between employee relationship scores and the number of movies they have in common. If two employees have no movies in common it should be treated as a 0, not a missing value, and should be included in the correlation calculation.
# This function should return a float.
def answer_four():
    Rel = nx.read_edgelist('Employee_Relationships.txt' ,data=[('relationship_score', int)])

    #Rel_df = pd.DataFrame(Rel.edges(data=True), columns=['From', 'To', 'relationship_score'])
    x = Rel.edges(data=True)
    y = list(x)
    Rel_df = pd.DataFrame(y, columns=['From', 'To', 'relationship_score'])    
   
    G = answer_three()
    
    #G_df = pd.DataFrame(G.edges(data=True), columns=['From', 'To', 'movies_score'])
    a = G.edges(data=True)
    b = list(a)
    G_df = pd.DataFrame(b, columns=['From', 'To', 'movies_score'])
    
    G_copy_df = G_df.copy()
    
    G_copy_df.rename(columns={"From":"From1", "To":"From"}, inplace=True)
    G_copy_df.rename(columns={"From1":"To"}, inplace=True)
    G_final_df = pd.concat([G_df, G_copy_df])
    final_df = pd.merge(G_final_df, Rel_df, on = ['From', 'To'], how='right')
    final_df['movies_score'] = final_df['movies_score'].map(lambda x: x['weight'] if type(x)==dict else None)
    final_df['relationship_score'] = final_df['relationship_score'].map(lambda x: x['relationship_score'])
    final_df['movies_score'].fillna(value=0, inplace=True)
    return final_df['movies_score'].corr(final_df['relationship_score'])

# answer_four()
