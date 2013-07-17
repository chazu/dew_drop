####################
# at runtime, we:
# will be instantiating items/components
# will NOT be instantiating new behaviors
# will NOT be instantiating new requirements
# WILL be assembling existing requirements and behaviors into new components..
import os
from sys import stdout

from behaviors.provide_fuel import ProvideFuel
from behaviors.propel_via_combustion import PropelViaCombustion
from behaviors.add_liquid import AddLiquid
from behaviors.remove_liquid import RemoveLiquid
from behaviors.impel_liquid import ImpelLiquid

from component import Component
from item import Item
from condition import Condition

from environment import Environment

class FuelTank(Component):

    name = "Fuel Tank"
    def __init__(self):
        super(FuelTank, self).__init__()
        self.name = "Fuel Tank"
        self.register_behavior(RemoveLiquid()) #Register the module containing the methods for the behavior
        self.register_behavior(AddLiquid())
        self.flags = ["IS_CONTAINER","CAN_CONTAIN_LIQUID"]
        self.contents = 500 #liters?

        self.item_input = None
        self.item_output = None

class FuelPump(Component):
    
    name = "Fuel Pump"
    def __init__(self):
        super(FuelPump, self).__init__()
        self.name = "Fuel Pump"
        self.flags = []

        self.item_input = None
        self.item_output = None

class Pipeline(Component):

    name = "Pipeline"
    def __init__(self):
        super(Pipeline, self).__init__()
        self.name = "Pipeline"
        self.flags = ["IS_LIQUID_CONVEYANCE"]

        self.item_input = None
        self.item_output = None

class FuelPumpAssembly(Component):

    name = "Fuel Pump Assembly"
    def __init__(self):
        super(FuelPumpAssembly, self).__init__()
        self.name = "Fuel Pump Assembly"
        self.register_component(FuelPump())
        self.register_component(Pipeline())

        self.register_behavior(ImpelLiquid())

class CombustionChamber(Component):

    name = "Combustion Chamber"
    def __init__(self):
        super(CombustionChamber, self).__init__()
        self.name = "Combustion Chamber"
        self.register_behavior(PropelViaCombustion())

        self.item_input = None
        self.item_output = None

        self.fuel_unit_to_thrust_ratio = 1.5 # In newtons
        self.fuel_unit_consumption_per_cycle = 10

class RocketEngine(Item):

    name = "Rocket Engine"
    def __init__(self, config_dict=None):
        super(RocketEngine, self).__init__(config_dict)
        self.name = "Rocket Engine"

if __name__ == "__main__":

    os.system('cls' if os.name=='nt' else 'clear') 

    tank = FuelTank()
    tank.report()

    chamber = CombustionChamber()
    chamber.report()

    pump_assembly = FuelPumpAssembly()
    pump_assembly.describe_behaviors()

    pump_assembly.item_input = tank
    pump_assembly.item_output = chamber

    pump_assembly.report()

    #assemble the engine:

    rocket = RocketEngine({'longevity': 100,
                           'durability_coefficient': 0.5,
                           'unreliability_threshold': 0.25,
                           'failure_threshold': 0.10,
                           'accuracy_coefficient':0.2 })

    rocket.register_component(pump_assembly)
    rocket.register_component(tank)
    rocket.register_component(chamber)

    pump_assembly.plug_out_from(tank)
    pump_assembly.plug_into(chamber)

    rocket.report()

    # Give the rocketship a position (via its environment object)
    rocket.register_environment(Environment('space'))
    rocket.environment.register_variable('position', 100)

    #Fire the engine!
    print("Current position: " + str(rocket.environment.position))
    rocket.execute_behavior(rocket.behaviors[0])
    print("Current position: " + str(rocket.environment.position))

    while rocket.longevity > 0:
        print("Rocket Longevity:" + str(rocket.longevity))
        rocket.execute_behavior(rocket.behaviors[0])
