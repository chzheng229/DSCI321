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



