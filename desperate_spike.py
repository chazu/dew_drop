
class AccessSystems(Behavior):

    requirements = []
    input_requirements = []
    output_requirements = []
    name = "Access Systems"
    aggregates_to_item = True
    description = """
    See all the attached systems
    """

    @staticmethod
    def behave(component, **kwargs):

    @staticmethod
    def on_registration(container, **kwargs):
        pass

computer = Item()

motherboard = Component()
motherboard.register_behavior(AccessSystems)
psu = Component()
gpu = Component()
cpu = Component()
ram = Component()

computer.register_component(cpu)
computer.register_component(gpu)
computer.register_component(ram)
computer.register_component(psu)
computer.register_component(motherboard)

psu.plug_into(cpu)
psu.plug_into(gpu)
psu.plug_into(motherboard)
ram.plug_into(motherboard)
