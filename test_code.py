from student_code2 import BinaryTree

tree = BinaryTree()

# Build the tree from the assignment's diagram
tree.add_node_left("8", 8)  # root, no parent
tree.add_node_left("71", 71, "8")
tree.add_node_right("41", 41, "8")
tree.add_node_left("31", 31, "71")
tree.add_node_right("10", 10, "71")
tree.add_node_left("11", 11, "41")
tree.add_node_right("16", 16, "41")
tree.add_node_left("46", 46, "31")
tree.add_node_right("51", 51, "31")
tree.add_node_left("31b", 31, "10")  # distinct node id, since "31" is already used
tree.add_node_right("21", 21, "10")
tree.add_node_left("13", 13, "11")

# Sanity checks
print("Left child of 8 (expect '71'):", tree.get_node_left("8"))
print("Right child of 8 (expect '41'):", tree.get_node_right("8"))
print("Left child of 71 (expect '31'):", tree.get_node_left("71"))
print("Right child of 41 (expect '16'):", tree.get_node_right("41"))

# Visualize it
tree.plot_graph()