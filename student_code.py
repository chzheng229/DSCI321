# DSCI321 Coding Assignment 1 - Charlie Zheng

# Defined below is the nested dictionary that contains all the nodes and their weights for each of the paths.

GRAPH = {
    "a": {"b":1, "d":5},
    "b": {"c":2, "f":5},
    "c": {"e":1, "h":3},
    "d": {"f":3},
    "e": {"d":3, "i":2},
    "f": {"e":4, "g":3, "i":3},
    "g": {"h":2, "k":2},
    "h": {"i":1, "j":2, "z": "4"},
    "i": {"j":4, "k":2},
    "j": {"c":1, "k":3, "z":4},
    "k": {"z":3}
}

def robot_navigation(nodes):
    """This function takes a list of strings denoted as nodes and has a robot travel along it
    The function weighs the paths that the robot takes and adds it up. It also checks for invalid node paths
    """
    # Invalidity Check
    #  if nodes is a list
    if not isinstance(nodes, list):
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
        next = nodes[i + 1]

        if current in visited:
            return -2
        visited.add(current)

        if
            #placeholder for now - coding the rest of the traversal logic later

