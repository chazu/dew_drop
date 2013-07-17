import sys
sys.path.append("./../")

from moka import *

from graph_proxy import GraphProxy
from util import *

##############################################
# Behaviors related to network functionality #
##############################################

from behaviors.base import Behavior
from behaviors.signal_handlers import network
from behaviors.requirements import requirement as req
from behaviors.requirements import network as network_req

state_namespace = "network"

initial_state = {
    "graph_proxy": (lambda x: GraphProxy.new(x))
}

class GetNetworkHosts(Behavior):

    requirements = [network_req.is_network_host]
    input_requirements = []
    output_requirements = []
    name = "Get Network Hosts"
    aggregates_to_item = True
    description = """
    Get all network hosts connected to component
    """

    @staticmethod
    def behave(component, **kwargs):
        # Return all nodes from all networks
        return component.state["graph_proxy"].nodes()

class QueryAdditionalHosts(Behavior):

    requirements = []
    input_requirements = []
    output_requirements = []
    name = "Query For Hosts"
    aggregates_to_item = True
    signal_handlers = "Foo", "Bar" #TODO Register signal handlers on registration
    description = """
    Request host info from directly connected hosts
    """

    @staticmethod
    def behave(component, **kwargs):
        for host in component.state.available_hosts:
            host.send('query_hosts', {host: component})
