# DSCI321 Coding Assignment 2 - Charlie Zheng
"""Representing graphs in functions using a variety of data structures"""

# Part 1 is defined below - list of sets

def part_1_graph():
    nodes_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
    graph = [set() for _ in range (len(nodes_dict))]

    graph[nodes_dict['a']].add(nodes_dict['b'])
    graph[nodes_dict['a']].add(nodes_dict['e'])
    graph[nodes_dict['b']].add(nodes_dict['c'])
    graph[nodes_dict['c']].add(nodes_dict['d'])
    graph[nodes_dict['c']].add(nodes_dict['e'])
    graph[nodes_dict['d']].add(nodes_dict['b'])

    return graph

# Part 2 is defined below - list of lists
def part_2_graph():
    """Represents the second graph & returns it as a list of lists"""
    nodes_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
    graph = [[] for _ in range (len(nodes_dict))]

    # Adding all the node paths into lists using .append (different methods for lists vs sets.)
    graph[nodes_dict['a']].append(nodes_dict['a'])
    graph[nodes_dict['a']].append(nodes_dict['b'])
    graph[nodes_dict['a']].append(nodes_dict['e'])
    graph[nodes_dict['b']].append(nodes_dict['c'])
    graph[nodes_dict['c']].append(nodes_dict['a'])
    graph[nodes_dict['c']].append(nodes_dict['d'])
    graph[nodes_dict['c']].append(nodes_dict['e'])
    graph[nodes_dict['e']].append(nodes_dict['d'])

    return graph



