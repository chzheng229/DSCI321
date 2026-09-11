class VersatileDigraph:
    def __init__(self):
        # Initialization of the class
        self.nodes = {}

        self.edges = {}

        self.edge_names = {}

    def add_node(self, node_id, node_value = 0):
        # Method to add nodes that don't already exist in the graph - also serves as a check against duplicate nodes
        if node_id not in self.nodes:
            self.nodes[node_id] = node_value

    def add_edge(self, start_node_id, end_node_id, start_node_value = 0, end_node_value = 0, edge_name=None, edge_weight = 0):
        self.add_node(start_node_id, start_node_value)
        self.add_node(end_node_id, end_node_value)

        # If edge name isn't supplied by user - names the edge for you.
        if edge_name is None:
            counter = 1
            candidate_name = f"edge{counter}"
            while candidate_name in self.edge_names.get(start_node_id, {}):
                counter += 1
                candidate_name = f"edge{counter}"
            edge_name = candidate_name

        








