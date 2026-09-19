# DSCI321 W3 Assignment - Charlie Zheng
"""Implementation of the VersatileDigraph class for DSCI321 Week 3."""
class VersatileDigraph:
    """Class to represent a digraph, with edge weights, edge names, node id, node value, etc."""

    def __init__(self):
        """Initialize the digraph with empty dicts for nodes edges and edge names."""
        self.nodes = {}
        self.edges = {}
        self.edge_names = {}
        self.next_edge_counter = {}  # start_node_id -> next number to try for auto-naming

    def add_node(self, node_id, node_value = 0):
        """ Add a node to the digraph """
        # Adds nodes that don't exist in the graph, serves as a check against duplicate nodes
        if node_id not in self.nodes:
            self.nodes[node_id] = node_value

    def add_edge(self, start_node_id, end_node_id, start_node_value=0,
                 end_node_value=0, edge_name=None, edge_weight=0):
        """ Add an edge to the digraph """
        self.add_node(start_node_id, start_node_value)
        self.add_node(end_node_id, end_node_value)

        # If edge name isn't supplied by user - names the edge for you.
        if edge_name is None:
            counter = self.next_edge_counter.get(start_node_id, 1)
            candidate_name = f"edge{counter}"
            while candidate_name in self.edge_names.get(start_node_id, {}):
                counter += 1
                candidate_name = f"edge{counter}"
            edge_name = candidate_name
            self.next_edge_counter[start_node_id] = counter + 1
        else:
            if edge_name in self.edge_names.get(start_node_id, {}):
                raise ValueError("Edge name already exists")

        if start_node_id not in self.edges:
            self.edges[start_node_id] = {}

        if start_node_id not in self.edge_names:
            self.edge_names[start_node_id] = {}

        self.edges[start_node_id][end_node_id] = {"weight": edge_weight, "name": edge_name}
        self.edge_names[start_node_id][edge_name] = end_node_id

    def get_nodes(self):
        """ Return a list of all nodes """
        # Returns the list of nodes (which are keys) as a list.
        return list(self.nodes.keys())

    def get_edge_weight(self, start_node_id, end_node_id):
        """ Return the edge weight of the edge between two nodes """
        # Returns the weight of a specific edge using the start and end node to search the dict
        return self.edges[start_node_id][end_node_id]["weight"]

    def get_node_value(self, node_id):
        """ Return the value of the node """
        # Returns the value of a node
        return self.nodes[node_id]

    def print_graph(self):
        """ Print the digraph using nodes and edges - returns as text"""
        for node_id in self.get_nodes():
            node_value = self.get_node_value(node_id)
            print(f"Node {node_id} with value {node_value}")

        for start_node_id, edges_from_start in self.edges.items():
            for end_node_id, edge_info in edges_from_start.items():
                weight = edge_info["weight"]
                name = edge_info["name"]
                message = (f"Edge from {start_node_id} to {end_node_id} "
                           f"with weight {weight} and name {name}")
                print(message)

    def successors(self, node_id):
        """Return a list of nodes that immediately succeed the given node."""
        return [end_node for end_node in self.edges.get(node_id, {})]

    def predecessors(self, node_id):
        """Return a list of nodes that immediately precede the given node."""
        return [start_node for start_node, edges_from_start in self.edges.items() if node_id in edges_from_start]

    def successor_on_edge(self, start_node_id, edge_name):
        """Return the node that immediately succeed the given edge."""
        return self.edge_names[start_node_id][edge_name]

    def out_degree(self, node_id):
        """Return the number of outgoing edges from the given node."""
        return len(self.successors(node_id))

    def in_degree(self, node_id):
        """Return the number of incoming edges to the given node."""
        return len(self.predecessors(node_id))
