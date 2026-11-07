from student_code import SpanningTreeGraph

g = SpanningTreeGraph()
edges = [("a", "b", 1), ("a", "d", 3), ("a", "e", 22), ("a", "g", 23),
         ("b", "c", 2), ("b", "d", 12), ("b", "g", 36), ("c", "d", 5),
         ("c", "e", 22), ("c", "f", 18), ("c", "g", 12), ("d", "e", 10),
         ("d", "f", 6), ("e", "f", 4), ("f", "g", 9)]
for u, v, w in edges:
    g.add_edge(u, v, edge_weight=w)

tree = g.spanning_tree("a")
print(tree)
print(sum(g.get_edge_weight(p, n) for n, p in tree.items() if p is not None))
