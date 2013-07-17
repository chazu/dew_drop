from component import Component, default_dict

class Item(Component):

    def __init__(self, config_dict=default_dict):
        super(Item, self).__init__(config_dict)
        pass

    def register_component(self, component):
        # Are all component behaviors available to item?
        self.components.append(component)
        component.container = self
        for behavior in component.behaviors:
            if behavior.aggregates_to_item == True:
                self.behaviors.append(behavior)

    def register_environment(self, environment):
        self.environment = environment
