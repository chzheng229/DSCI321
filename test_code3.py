from student_code import SortingTree



t = SortingTree()
for v in [50, 30, 70, 20, 40, 60, 80, 50]:
    t.insert(v)
print(t.traverse())

t.print_graph()