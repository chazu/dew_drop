import networkx as nx
import logging

logging.basicConfig(level=logging.DEBUG)

class GraphProxy:

    def __init__(self, component_list, undirected=False):

        self._graph = nx.DiGraph() if undirected == False else nx.Graph()
        self._graph.add_nodes_from(component_list)

    def nodes(self):
        return self._graph.nodes()

    def edges(self):
        return self._graph.edges()

    def is_contiguous(self):
        return nx.is_connected(self._graph.to_undirected())

    def add_node(self, thing):
        logging.debug("Adding node: " + thing.name)
        # Add thing to graph and set its graph proxy to us
        nodes_to_add = thing.graph_proxy.get_nodes()
        logging.debug("Nodes to add: " + str([x.name for x in nodes_to_add]))
        edges_to_add = thing.graph_proxy.get_edges()

        self._graph.add_nodes_from(nodes_to_add)
        self._graph.add_edges_from(edges_to_add)
        for node in nodes_to_add:
            node.graph_proxy = self

    def add_link(self, source, target):
        # unless target is in graph already, add it
        if not target in self._graph.nodes():
            self.add_node(target)
            # Now add the edge
        self._graph.add_edge(source, target)

    def get_components(self):
        return nx.weakly_connected_component_subgraphs(self._graph)

    def split_graphs(self):
        components = self.get_components()
        # for component in components:
        #     new_proxy = GraphProxy(component.nodes())
        #     for node in component.nodes():
        #         node.graph_proxy = new_proxy

    def remove_link(self, source, target):
        self._graph.remove_edge(source, target)
        if not self.is_contiguous():
            print "splitting!"
            self.split_graphs()

    def get_nodes(self):
        return self._graph.nodes()

    def get_edges(self):
        return self._graph.edges()

if __name__ == "__main__":

    from component import Component

    a = Component(name="a")
    b = Component(name="b")
    c = Component(name="c")
    d = Component(name="d")
    e = Component(name="e")
    f = Component(name="f")
    g = Component(name="g")

    b.plug_into(a)
    d.plug_into(b)
    c.plug_into(d)
    e.plug_into(f)
    e.plug_into(d)
    e.plug_into(g)

    e.graph_proxy.get_components()

    d.unplug_from(e)

    print str(e.graph_proxy.get_components()[1].nodes())
