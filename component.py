import copy

from moka import *
import texttable as tt
from graph_proxy import GraphProxy

import behaviors.requirements.requirement as req
from state import State
from component_collection import ComponentCollection

default_dict = {'longevity'                : 1000,
                'durability_coefficient'   : 0,
                'unreliability_threshold'  : 0,
                'failure_threshold'        : 0,
                'inaccuracy_rating'        : 0,
                'inaccuracy_offset'        : 0,
                'inaccuracy_growth_factor' : 0
            }

class Component(object):
    component_register = []

    def __init__(self, config_dict=default_dict, name=None):
        """
        """
        self.components = ComponentCollection()
        self.graph_proxy = GraphProxy([self])
        self.behaviors = []
        self.signal_handlers = {}
        self.name = name or "Untitled Component"
        self.state = State()

        # Durability/Longevity values
        self.longevity = config_dict['longevity'] or 1000
        self.current_longevity = config_dict['longevity'] or 1000
        self.durability_coefficient = config_dict['durability_coefficient'] or 0
        self.unreliability_threshold = config_dict['unreliability_threshold']
        self.failure_threshold = config_dict['failure_threshold']
        self.next_accuracy_offset = "TODO Insert random value in range of accuracy offset"
        self.inaccuracy_rating = config_dict['inaccuracy_rating'] # [in]Accuracy above reliability threshold
        self.inaccuracy_growth_factor = config_dict['inaccuracy_growth_factor']
        # TODO failure_chance_growth_factor (how does failure change change below failure threshold)

        # Add self to static class list
        Component.component_register.append(self)

    def item_inputs(self):
        "Get all the components with edges ending on this guy"
        return List(self.graph_proxy.predecessors(self))

    def item_outputs(self):
        return List(self.graph_proxy.successors(self))

    def duplexes(self):
        "All components which are both inputs and outputs"
        return List(set(self.item_inputs()).intersection(self.item_outputs()))

    def __deepcopy__(self, memo):
        return self

    def __str__(self):
        return self.name if self.name else "Untitled Component"

    ## POST-EXECUTION STATE MODIFICATION##############################
    def update_durability(self):
        self.current_longevity -= 1 * self.durability_coefficient
        # TODO if beneath unreliability threshold, adjust accuracy
        # TODO if beneath failure threshold, roll for failure and distribute damage

    ## REGISTRATION OF COMPONENTS/BEHAVIORS ##########################

    def register_behavior(self, behavior):
        self.behaviors.append(behavior)
        self.register_signal_handlers(behavior)
        self.register_initial_behavior_state(behavior)
        # TODO modify state depending on the behavior registered here

    def register_component(self, component):
        self.components.append(component)
        component.container = self

        # TODO Aggregate behaviors and state as necessary.
        # TODO Alter state with relevant variables, callbacks,
        # etc

    def register_initial_behavior_state(self, behavior):
        for key, value in behavior.initial_state:
            if hasattr(behavior.initial_state[key], '__call__'):
                self.state[key] = value(self)
            else:
                self.state[key] = value

    ## TESTING REQUIREMENTS ##########################################
    def test_requirements(self, behavior):
        return False not in [req.recursively_test_component(self, requirement) \
                             for requirement in behavior.requirements]


    ## BEHAVIOR EXECUTION ############################################
    def execute_behavior(self, behavior):
        if self.test_requirements(behavior):
            behavior.behave(self)
            self.update_durability()
            # TODO Change component/item state

    ## BEHAVIOR TESTING ###############################################
    def test_behavior_requirements(self, behavior):
        for requirement in behavior.requirements:
            recursively_test_requirement(self, requirement)

    ## REQUIREMENT TESTING #############################################
    def recursively_test_requirement(self, requirement):
        if requirement(component) == True:
            return True
        else:
            if len(component.components) == 0:
                return False
            else:
                for component in component.components:
                    recursively_test_component(component, requirement)

    def describe_behaviors(self):
        for behavior in self.behaviors:
            print(behavior.name)

    ## INPUTS & OUTPUTS ################################################

    def plug_into(self, other):
        "Add self to other's inputs, add other as output on self"
        self.graph_proxy.add_link(self, other)

    def plug_out_from(self, other):
        "Add self to other's outputs, add other as input on self"
        other.graph_proxy.add_link(other, self)

    def unplug_from(self, other):
        other.graph_proxy.remove_link(other, self)

    def establish_duplex(self, other):
        "Establish bidirectional communication"
        self.plug_into(other)
        self.plug_out_from(other)

    def register_signal_handlers(self, behavior):
        """
        Register callbacks to be executed when a signal is received
        via direct behavior execution.
        behavior - A behavior class with signal handlers
        """
        for handler in behavior.signal_handlers:
            self.signal_handlers[handler[0]] = getattr(handler[1], 'behave')

    ## DIRECT BEHAVIOR EXECUTION########################################
    def send(self, signal, args={}):
        """
        Receive a signal during the execution of a behavior which does
        not modify the environment directly, instead modifying connected
        components.
        """
        self.signal_handlers[signal](self, args)

    ## ACCURACY METHODS ################################################
    def get_next_inaccuracy(self):
        pass

    def get_inaccuracy_percentage(self):
        if self.current_longevity < ( self.longevity * self.unreliability_threshold ):
            return self.inaccuracy_rating ** ( self.get_pct_unreliable_longevity_remaining()  - self.inaccuracy_growth_factor )
        else:
            return self.inaccuracy_rating

    def get_pct_unreliable_longevity_remaining(self):
        return self.current_longevity / ( self.longevity * self.unreliability_threshold )

    def get_pct_unreliable_longevity_used(self):
        return 1 - self.get_pct_unreliable_longevity_remaining()

    ## DEBUGGING METHODS ###############################################

    def print_inputs_and_outputs(self):
        tab = tt.Texttable()
        tab.header(["INPUTS", "OUTPUTS"])
        tab.add_row([str([component.name + " " for component in self.item_inputs]),str([component.name + " " for component in self.item_outputs])])
        print tab.draw()

    def component_summary(self):
        for component in self.components:
            print component.name, " ", \
                str([x.name for x in component.item_inputs]), \
                str([x.name for x in component.item_outputs])

    def report(self):
        print "{{{COMPONENT: " + self.name + "}}}"
        print "++++++++++++++++COMPONENTS/INPUTS/OUTPUTS+++++++++++"
        self.component_summary()
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
        if len(self.behaviors) > 0:
            print "======BEHAVIORS======"
            tab = tt.Texttable()
            tab.header([ "Behavior","Requirements"])
            print self.behaviors
            for item in self.behaviors:
                tab.add_row([item.name,
                             [requirement for requirement in item.requirements]])
                print tab.draw()
        else:
            print "---NO BEHAVIORS---"
        print "++++++++++++++++INPUTS & OUTPUTS++++++++++++++++++++"
        self.print_inputs_and_outputs()
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
        if len(self.signal_handlers) > 0:
            print "======SIGNAL HANDLERS======"
            print "TODO Add this to report method"
