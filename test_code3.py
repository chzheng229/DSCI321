from student_code import SortingTree



t = SortingTree()
for v in [50, 30, 70, 20, 40, 60, 80, 50]:
    t.insert(v)
print(t.traverse())

t.print_graph()

t = SortingTree(5)
t.insert(3)
t.insert(7)
print(t.traverse())  # expect [3, 5, 7]
print(SortingTree().traverse())      # prints [] twice: once from print, once from your print()
t = SortingTree(5)
t.insert(3)
t.insert(7)
t.insert(5)
t.traverse()                         # prints [3, 5, 5, 7] once
t = SortingTree(5)
t.insert(3)
t.insert(7)
print(t.get_node_value(t.get_node_left("Root")))   # expect 3
print(t.get_node_value(t.get_node_right("Root")))  # expect 7
t.traverse()                                       # expect [3, 5, 7]