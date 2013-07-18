from graph_proxy import GraphProxy

class Network:
    """
    An abstraction of a network. Duh.
    """

    def __init__(self):

        self.graph_proxy = GraphProxy(self)

    def hosts(self):
        self.graph_proxy.nodes()


