import sys
sys.path.append("./../")
from moka import *

##############################################
# Behaviors related to network functionality #
##############################################

from behaviors.base import Behavior
from behaviors.signal_handlers import network
from behaviors.requirements import requirement as req
from behaviors.requirements import network as network_req

class GetNetworkHosts(Behavior):

    requirements = []
    input_requirements = []
    output_requirements = []
    name = "Get Network Hosts"
    aggregates_to_item = True
    description = """
    Get all network hosts connected to component
    """

    @staticmethod
    def behave(component, **kwargs):
        if component.state.has_flag("IS_NETWORK_LINK"):
            pass
        else:
            List(self.components.with_flag("IS_NETWORK_LINK")).map(lambda x: x.state
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
