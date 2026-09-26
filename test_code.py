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

# Test 6: duplicate edge name for the same start node should raise ValueError
try:
    g.add_edge("A", "C", edge_name="edge1")  # "edge1" already used for A -> should raise
    print("Test 6 FAILED - expected ValueError but none was raised")
except ValueError as e:
    print("Test 6 PASSED - correctly raised ValueError:", e)

# Test 7: predecessors, successors, successor_on_edge, indegree, outdegree
g2 = VersatileDigraph()
g2.add_edge("A", "B", edge_name="edge1", edge_weight=5)
g2.add_edge("A", "C", edge_name="edge2", edge_weight=2)
g2.add_edge("D", "B", edge_name="edge1", edge_weight=1)

print("Test 7 - successors of A (expect ['B', 'C']):", g2.successors("A"))
print("Test 7 - predecessors of B (expect ['A', 'D']):", g2.predecessors("B"))
print("Test 7 - successor_on_edge A, edge1 (expect 'B'):", g2.successor_on_edge("A", "edge1"))
print("Test 7 - outdegree of A (expect 2):", g2.out_degree("A"))
print("Test 7 - indegree of B (expect 2):", g2.in_degree("B"))
print("Test 7 - successors of Z, no edges (expect []):", g2.successors("Z"))
print("Test 7 - predecessors of Z, no edges (expect []):", g2.predecessors("Z"))

import graphviz

g3 = VersatileDigraph()
g3.add_node("Allentown", 66)
g3.add_node("Easton", 74)
g3.add_node("Bethlehem", 70)
g3.add_edge("Allentown", "Easton", edge_name="US22W", edge_weight=17)
g3.add_edge("Easton", "Allentown", edge_name="US22E", edge_weight=17)
g3.add_edge("Bethlehem", "Allentown", edge_name="Hanover", edge_weight=6)
g3.add_edge("Allentown", "Bethlehem", edge_name="Hanover", edge_weight=6)
g3.add_edge("Bethlehem", "Easton", edge_name="US22E", edge_weight=12)
g3.add_edge("Easton", "Bethlehem", edge_name="Freemansburg", edge_weight=12)
g3.plot_graph()

from bokeh.plotting import figure, show

g3.plot_edge_weights()