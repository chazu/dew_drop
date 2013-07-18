import sys
sys.path.append("./../")
sys.path.append("./../../")

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
    name = "Get Network Hosts"
    aggregates_to_item = True
    description = "Get all network hosts connected to component"
    signal_handlers = []

    @staticmethod
    def behave(component, **kwargs):
        # Return all nodes from all networks
        return component.state["graph_proxy"].nodes()


class AcknowledgeConnectionRequest(Behavior):

    requirements = [network_req.is_network_host]
    name = "Acknowlege Connection Request"
    aggregates_to_item = True
    description = "Add the host to your network"
    signal_handlers = []

    @staticmethod
    def behave(component, **kwargs):
        component.state["network"].graph_proxy.add_link(
            kwargs["target"])


class DisconnectHost(Behavior):

    requirements = [network_req.is_network_host]
    name = "Disconnect Host"
    aggregates_to_item = True
    description = "Disconnect Host"
    signal_handlers = []

    @staticmethod
    def behave(component, **kwargs):
        component.state["network"].graph_proxy.remove_link(
            kwargs["target"])

