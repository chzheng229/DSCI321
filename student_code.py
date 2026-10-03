"""Implementing a binary tree class, inheriting from VersatileDigraph."""
# Week 6 DSCI321 Coding - Binary Tree Class - Charlie Zheng
from student_code import VersatileDigraph

class BinaryTree(VersatileDigraph):
    """A binary tree built on top of VersatileDigraph, using left and right as edge names."""
    # Doesn't need a init method - inherits one that works

    def add_node_left(self, child_id, child_value, parent_id=None):
        """add a left child node - if no parent is given, adds a standalone root node."""
        if parent_id is None:
            self.add_node(child_id, child_value)
        else:
            self.add_edge(start_node_id=parent_id, end_node_id=child_id,
                          end_node_value=child_value, edge_name="left")

    def add_node_right(self, child_id, child_value, parent_id=None):
        """add a right child node - if no parent is given, adds a standalone root node."""
        if parent_id is None:
            self.add_node(child_id, child_value)
        else:
            self.add_edge(start_node_id=parent_id, end_node_id=child_id,
                          end_node_value=child_value, edge_name="right")

    def get_node_left(self, parent_id):
        """returns the id of the left child node for parent node given its parent id."""
        return self.successor_on_edge(start_node_id=parent_id,edge_name="left")

    def get_node_right(self, parent_id):
        """returns the id of the right child node for parent node given its parent id."""
        return self.successor_on_edge(start_node_id=parent_id,edge_name="right")
