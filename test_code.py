from student_code import VersatileDigraph

g = VersatileDigraph()

# Test 1: node value should be preserved, not reset by add_edge
g.add_node("A", 10)
g.add_edge("A", "B", edge_weight=5, edge_name="edge1")
print("Test 1 - A's value should be 10:", g.get_node_value("A"))

# Test 2: auto-naming should avoid collisions
g.add_edge("A", "C")  # no name given -> should become "edge2" (edge1 taken)
g.add_edge("A", "D")  # no name given -> should become "edge3"
print("Test 2 - edge_names for A:", g.edge_names["A"])

# Test 3: get_edge_weight should return the correct weight
print("Test 3 - weight of A->B:", g.get_edge_weight("A", "B"))

# Test 4: get_nodes should list every node added so far
print("Test 4 - all nodes:", g.get_nodes())

# Test 5: full print_graph output
print("Test 5 - full graph:")
g.print_graph()