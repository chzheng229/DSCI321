from student_code import DAG

g = DAG()
for a, b in [("shirt", "tie"), ("shirt", "pants"), ("shirt", "vest"), ("shirt", "jacket"),
             ("pants", "belt"), ("pants", "shoes"), ("socks", "shoes"),
             ("tie", "jacket"), ("belt", "jacket"), ("vest", "jacket")]:
    g.add_edge(a, b)

print(list(g.dfs("shirt")))
print(list(g.bfs("shirt")))
print(g.top_sort())

for a, b in [("jacket", "shirt"), ("belt", "pants"), ("shirt", "shirt")]:
    try:
        g.add_edge(a, b)
        print("FAILED - no error for", a, b)
    except ValueError as e:
        print("PASSED:", e)