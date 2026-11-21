from student_code import MaxFlowGraph

g = MaxFlowGraph()
for u, v, c in [("s", "a", 10), ("s", "b", 5), ("a", "b", 15),
                ("a", "t", 5), ("b", "t", 10)]:
    g.add_edge(u, v, edge_weight=c)

value, flow = g.max_flow("s", "t")
print(value)   # expect 15
print(flow)    # no edge should exceed its capacity

print(g.res_graph({}).get_edge_weight("s", "a"))                  # 10 (no flow yet)
r = g.res_graph({("s", "a"): 4})
print(r.get_edge_weight("s", "a"), r.get_edge_weight("a", "s"))   # 6 and 4
print(g.bfs("s", "t") is not None, g.bfs("t", "s"))               # True None