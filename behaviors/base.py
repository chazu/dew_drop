class Behavior(object):
    behaviors = []
    requirements = []
    input_requirements = []
    output_requirements = []
    name = "Unknown Behavior"
    aggregates_to_item = False
    def __init__(self):
        self.requirements = []
        self.input_requirements = []
        self.output_requirements = []
        self.name = "Unknown Behavior"
        self.aggregates_to_item = False

        Behavior.behaviors.append(self)

    def behave(self, component):
        pass
