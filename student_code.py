# DSCI321 W10 Assignment - Charlie Zheng
"""Implementation of the VersatileDigraph class and all the subclasses under for DSCI321 Week 10."""
from collections import deque
import graphviz
from bokeh.plotting import figure, show


class VersatileDigraph:
    """Class to represent a digraph, with edge weights, edge names, node id, node value, etc."""

    def __init__(self):
        """Initialize the digraph with empty dicts for nodes edges and edge names."""
        self.nodes = {}
        self.edges = {}
        self.edge_names = {}
        self.next_edge_counter = {}  # start_node_id -> next number to try for auto-naming

    def add_node(self, node_id, node_value=0):
        """ Add a node to the digraph """

        # checks if node_id is a string and raises a typeerror if not
        if not isinstance(node_id, str):
            raise TypeError(f"node_id must be a string, got {type(node_id).__name__}")

        # checks of node_value is a integer and raises a typeerror if not
        if not isinstance(node_value, (int, float)):
            raise TypeError(f"node_value must be a number, got {type(node_value).__name__}")
        # Adds nodes that don't exist in the graph, serves as a check against duplicate nodes
        if node_id not in self.nodes:
            self.nodes[node_id] = node_value

    def add_edge(self, start_node_id, end_node_id, start_node_value=0,
                 end_node_value=0, edge_name=None, edge_weight=0):
        """ Add an edge to the digraph """

        # Raises typeerror for incorrect types of arguments
        if not (isinstance(edge_name, str) or edge_name is None):
            raise TypeError(f"edge_name must be a string or None, got {type(edge_name).__name__}")

        if not isinstance(start_node_id, str):
            raise TypeError(f"start_node_id must be a string, got {type(start_node_id).__name__}")

        if not isinstance(end_node_id, str):
            raise TypeError(f"end_node_id must be a string, got {type(end_node_id).__name__}")

        if not isinstance(start_node_value, (int, float)):
            raise TypeError(
                f"start_node_value must be a number, got {type(start_node_value).__name__}"
            )

        if not isinstance(end_node_value, (int, float)):
            raise TypeError(f"end_node_value must be a number, got {type(end_node_value).__name__}")

        if not isinstance(edge_weight, (int, float)):
            raise TypeError(f"edge_weight must be a number, got {type(edge_weight).__name__}")

        if edge_weight < 0:
            raise ValueError(f"edge_weight must be non-negative, got {edge_weight}")

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

        if not isinstance(start_node_id, str):
            raise TypeError(f"start_node_id must be a string, got {type(start_node_id).__name__}")

        if not isinstance(end_node_id, str):
            raise TypeError(f"end_node_id must be a string, got {type(end_node_id).__name__}")

        if start_node_id not in self.nodes or end_node_id not in self.nodes:
            raise KeyError(f"One of your nodes {start_node_id}, or {end_node_id} does not exist")

        if end_node_id not in self.edges.get(start_node_id, {}):
            raise KeyError(f"No edge exists from '{start_node_id}' to '{end_node_id}'")

        # Returns the weight of a specific edge using the start and end node to search the dict
        return self.edges[start_node_id][end_node_id]["weight"]

    def get_node_value(self, node_id):
        """ Return the value of the node """
        if not isinstance(node_id, str):
            raise TypeError(f"node_id must be a string, got {type(node_id).__name__}")
        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} does not exist")
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
        if not isinstance(node_id, str):
            raise TypeError(f"node_id must be a string, got {type(node_id).__name__}")

        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} does not exist")

        return [end_node for end_node in self.edges.get(node_id, {})]

    def predecessors(self, node_id):
        """Return a list of nodes that immediately precede the given node."""
        if not isinstance(node_id, str):
            raise TypeError(f"node_id must be a string, got {type(node_id).__name__}")

        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} does not exist")

        return [start_node for start_node, edges_from_start in self.edges.items()
                if node_id in edges_from_start]

    def successor_on_edge(self, start_node_id, edge_name):
        """Return the node that immediately succeed the given edge."""
        if not isinstance(start_node_id, str):
            raise TypeError(f"start_node_id must be a string, got {type(start_node_id).__name__}")

        if not isinstance(edge_name, str):
            raise TypeError(f"edge_name must be a string, got {type(edge_name).__name__}")

        if start_node_id not in self.nodes:
            raise KeyError(f"Node {start_node_id} does not exist")

        if edge_name not in self.edge_names.get(start_node_id, {}):
            raise KeyError(f"No edge exists from '{start_node_id}' with name {edge_name}'")

        return self.edge_names[start_node_id][edge_name]

    def out_degree(self, node_id):
        """Return the number of outgoing edges from the given node."""
        if not isinstance(node_id, str):
            raise TypeError(f"node_id must be a string, got {type(node_id).__name__}")

        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} does not exist")

        return len(self.successors(node_id))

    def in_degree(self, node_id):
        """Return the number of incoming edges to the given node."""
        if not isinstance(node_id, str):
            raise TypeError(f"node_id must be a string, got {type(node_id).__name__}")

        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} does not exist")

        return len(self.predecessors(node_id))

    def plot_graph(self):
        """Plots the digraph using graphviz """
        dot = graphviz.Digraph()
        for node_id in self.get_nodes():
            node_value = self.get_node_value(node_id)
            dot.node(node_id, label=f"{node_id}:{node_value}")

        for start_node_id, edges_from_start in self.edges.items():
            for end_node_id, edge_info in edges_from_start.items():
                weight = edge_info["weight"]
                name = edge_info["name"]
                dot.edge(start_node_id, end_node_id, label=f"{name}:{weight}")

        dot.render("graph_output", view=True)

    def plot_edge_weights(self):
        """Plots the edge weights as a bar graph using Bokeh"""
        labels = []
        weights = []

        for start_node_id, edges_from_start in self.edges.items():
            for _, edge_info in edges_from_start.items():
                weights.append(edge_info["weight"])
                labels.append(f"{start_node_id}-{edge_info['name']}")

        p = figure(x_range=labels, title="Edge Weights")
        p.xaxis.major_label_orientation = "vertical"
        p.vbar(x=labels, top=weights, width=0.5)
        show(p)


class SortableDigraph(VersatileDigraph):
    """A subclass of previous week's versatile digraph - can be topologically sorted."""

    def top_sort(self):
        """Returns a list of the nodes in the graph topologically sorted."""

        count = {u: self.in_degree(u) for u in self.get_nodes()}
        queue = [u for u in self.get_nodes() if count[u] == 0]
        results = []
        while queue:
            u = queue.pop()
            results.append(u)
            for v in self.successors(u):
                count[v] -= 1
                if count[v] == 0:
                    queue.append(v)
        if len(results) != len(self.get_nodes()):
            raise ValueError("Graph has a cycle, this is unable to be topologically sorted.")
        return results

class TraversableDigraph(SortableDigraph):
    """A sortable digraph that can be traversed depth-first or breadth-first."""

    def dfs(self, start_node_id):
        """Yield nodes depth-first from start_node_id, not including the start node."""
        if start_node_id not in self.nodes:
            raise KeyError(f"Node {start_node_id} does not exist")
        visited, stack = set(), [start_node_id]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack.extend(self.successors(node))
            if node != start_node_id:
                yield node

    def bfs(self, start_node_id):
        """Yield nodes breadth-first from start_node_id, not including the start node."""
        if start_node_id not in self.nodes:
            raise KeyError(f"Node {start_node_id} does not exist")
        visited, queue = set(), deque([start_node_id])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            queue.extend(self.successors(node))
            if node != start_node_id:
                yield node

class DAG(TraversableDigraph):
    """A traversable digraph that refuses any edge that would create a cycle."""

    def add_edge(self, start_node_id, end_node_id, start_node_value=0,
                 end_node_value=0, edge_name=None, edge_weight=0):
        """Add an edge, raising ValueError if it would create a cycle."""
        if start_node_id == end_node_id:
            raise ValueError("An edge from a node to itself would create a cycle")
        if start_node_id in self.nodes and end_node_id in self.nodes:
            if start_node_id in self.bfs(end_node_id):
                raise ValueError(
                    f"Edge {start_node_id} -> {end_node_id} would create a cycle"
                )
        super().add_edge(start_node_id, end_node_id, start_node_value,
                         end_node_value, edge_name, edge_weight)


class MaxFlowGraph(TraversableDigraph):
    """A traversable digraph that can compute maximum flow (Edmonds-Karp)."""

    def res_graph(self, f):
        """Return the residual graph (a MaxFlowGraph) for the flow dict f.

        f maps (start, end) -> flow on that edge. Edge weights are capacities.
        """
        if not isinstance(f, dict):
            raise TypeError(f"f must be a dict, got {type(f).__name__}")

        residual = {}
        for start, edges_from_start in self.edges.items():
            for end, edge_info in edges_from_start.items():
                flow = f.get((start, end), 0)
                residual[(start, end)] = (residual.get((start, end), 0)
                                          + edge_info["weight"] - flow)
                residual[(end, start)] = residual.get((end, start), 0) + flow

        graph = MaxFlowGraph()
        for node_id, node_value in self.nodes.items():
            graph.add_node(node_id, node_value)
        for (start, end), capacity in residual.items():
            graph.add_edge(start, end, edge_weight=capacity)
        return graph

    def bfs(self, start_node, end_node=None):  # pylint: disable=arguments-differ,arguments-renamed
        """Find a path with spare capacity from start_node to end_node.

        Returns a dict of node -> parent, or None if end_node cannot be reached.
        If end_node is None, the parents of every reachable node are returned.
        """
        parents = {start_node: None}
        if start_node == end_node:
            return parents
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            for neighbor in self.successors(node):
                if neighbor in parents or self.get_edge_weight(node, neighbor) <= 0:
                    continue
                parents[neighbor] = node
                if neighbor == end_node:
                    return parents
                queue.append(neighbor)
        return parents if end_node is None else None

    def max_flow(self, s, t):
        """Return (max flow value, flow dict) from source s to sink t."""
        for node in (s, t):
            if node not in self.nodes:
                raise KeyError(f"Node {node} does not exist")
        if s == t:
            raise ValueError("Source and sink must be different nodes")

        flow = {(u, v): 0 for u, edges in self.edges.items() for v in edges}
        total = 0
        while True:
            parents = self.res_graph(flow).bfs(s, t)
            if parents is None:
                break
            path = []
            node = t
            while parents[node] is not None:
                path.append((parents[node], node))
                node = parents[node]

            residual = self.res_graph(flow)
            bottleneck = min(residual.get_edge_weight(u, v) for u, v in path)
            for u, v in path:
                remaining = bottleneck
                if (u, v) in flow:
                    push = min(remaining, self.get_edge_weight(u, v) - flow[(u, v)])
                    flow[(u, v)] += push
                    remaining -= push
                if remaining > 0:
                    flow[(v, u)] -= remaining
            total += bottleneck
        return total, flow
