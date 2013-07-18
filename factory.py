import json
import logging

from component import Component
# TODO package stuff in exports properly
from behaviors.exports import network as exports

logging.basicConfig(level=logging.DEBUG)

class Factory:
    """
    Creates instances of components based on spec
    """

    def __init__(self):
        pass

    def create_from_file(self, filepath):
        spec = json.load(open(filepath))
        component = Component(spec["config"], spec["name"])
        for behavior in spec["behaviors"]:
            # TODO package stuff in exports properly
            # target = getattr(exports, behavior[0])
            target = getattr(exports, behavior[1])
            logging.debug("Registering behavior: " + str(target))
            component.register_behavior(target)
        return component

factory = Factory()

a = factory.create_from_file("factory_test.json")
print str(a.state["graph_proxy"])
