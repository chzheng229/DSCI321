from student_code import SortableDigraph

g = SortableDigraph()
g.add_edge("shirt", "tie")
g.add_edge("shirt", "pants")
g.add_edge("shirt", "vest")
g.add_edge("shirt", "jacket")
g.add_edge("pants", "belt")
g.add_edge("pants", "shoes")
g.add_edge("socks", "shoes")
g.add_edge("tie", "jacket")
g.add_edge("belt", "jacket")
g.add_edge("vest", "jacket")

order = g.top_sort()
print(order)

c = SortableDigraph()
c.add_edge("a", "b")
c.add_edge("b", "a")
try:
    c.top_sort()
    print("FAILED - no error raised")
except ValueError as e:
    print("PASSED:", e)