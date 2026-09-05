# DSCI321 Coding Assignment 2 - Charlie Zheng
"""Representing graphs in functions using a variety of data structures"""

# Part 1 is defined below - list of sets

def part_1_graph():
    """Represents the first graph & returns it as a list of sets"""
    nodes_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
    graph = [set() for _ in range (len(nodes_dict))]

    # adding all the paths to sets
    graph[nodes_dict['a']].add('b')
    graph[nodes_dict['a']].add('e')
    graph[nodes_dict['b']].add('c')
    graph[nodes_dict['c']].add('d')
    graph[nodes_dict['c']].add('e')
    graph[nodes_dict['d']].add('b')

    return graph

# Part 2 is defined below - list of lists
def part_2_graph():
    """Represents the second graph & returns it as a list of lists"""
    nodes_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
    graph = [[] for _ in range (len(nodes_dict))]

    # Adding all the node paths into lists using .append (different methods for lists vs sets.)
    graph[nodes_dict['a']].append('a')
    graph[nodes_dict['a']].append('b')
    graph[nodes_dict['a']].append('e')
    graph[nodes_dict['b']].append('c')
    graph[nodes_dict['c']].append('a')
    graph[nodes_dict['c']].append('d')
    graph[nodes_dict['c']].append('e')
    graph[nodes_dict['e']].append('d')

    return graph

# Part 3 is defined below - list of dicts
def part_3_graph():
    """Represents the third graph & returns it as a list of dicts"""
    nodes_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
    graph = [{} for _ in range (len(nodes_dict))]

    # adding all the paths to the dictionaries - also assigning the weights for the paths
    graph[nodes_dict['a']]['a'] = 8
    graph[nodes_dict['a']]['b'] = 1
    graph[nodes_dict['a']]['e'] = 4
    graph[nodes_dict['b']]['c'] = 3
    graph[nodes_dict['c']]['a'] = 2
    graph[nodes_dict['c']]['e'] = 4

    return graph

# Part 4 is defined below - dict of sets
def part_4_graph():
    """Represents the fourth graph & returns it as a dict of sets"""
    graph = {
        'a': set(),
        'b': set(),
        'c': set(),
        'd': set(),
        'e': set(),
    }
    # adding all the paths into the sets
    graph['a'].add('a')
    graph['a'].add('b')
    graph['a'].add('e')
    graph['b'].add('c')
    graph['c'].add('a')

    return graph


# Part 5 is defined below - dict of dicts
def part_5_graph():
    """Represents the fifth graph & returns it as a dict of dicts"""
    graph = {
        'a': {},
        'b': {},
        'c': {},
        'd': {},
        'e': {},
    }
    # adding all the node paths into dicts
    graph['a']['b'] = 5
    graph['b']['e'] = 3
    graph['e']['b'] = 2
    graph['e']['a'] = 6

    return graph
