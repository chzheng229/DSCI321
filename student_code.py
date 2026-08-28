# DSCI321 Coding Assignment 1 - Charlie Zheng
"""Robot Navigation Assignment - has a robot travel along given path in weighted graph"""

# Defined below is the nested dictionary w/ nodes and weights.

GRAPH = {
    "a": {"b":1, "d":5},
    "b": {"c":2, "f":5},
    "c": {"e":1, "h":3},
    "d": {"f":3},
    "e": {"d":3, "i":2},
    "f": {"e":4, "g":3, "i":3},
    "g": {"h":2, "k":2},
    "h": {"i":1, "j":2, "z": 4},
    "i": {"j":4, "k":2},
    "j": {"c":1, "k":3, "z":4},
    "k": {"z":3},
    "z": {}
}

def robot_navigation(nodes):
    """Function takes a list of strings as nodes and has a robot travel along it
    Function weighs the paths that the robot takes ands sums. Also checks for invalid node paths
    """
    # Invalidity Check
    #  if nodes is a list
    if not isinstance(nodes, list):
        return -1

    # Check if nodes is not empty
    if len(nodes) == 0:
        return -1

    # Check if nodes is all strings
    if not all(isinstance(node, str) for node in nodes):
        return -1

    # Check if Nodes not starting at A
    if nodes[0] != 'a':
        return -1

    # Check if all the nodes provided in argument are valid nodes
    if not all(n in GRAPH for n in nodes):
        return -1

    # Node Traversal Logic
    visited = set()
    total_weight = 0

    for i in range(len(nodes) - 1):
        current = nodes[i]
        next_node = nodes[i + 1]


        # Checks for cyclical nature, by checking current node against the set of visited nodes
        # Also checks for cycles with the last node in the list causing it to be cyclical
        if current in visited or next_node in visited:
            return -2
        visited.add(current)


        # Checks for invalid paths (i.e. node list {a, z})
        if next_node not in GRAPH[current]:
            return -1

        total_weight += GRAPH[current][next_node]


    if nodes[-1] == "z":
        return total_weight, "z"
    return 0, nodes[-1]
