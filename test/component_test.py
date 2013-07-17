import sys
sys.path.append("./../")

import networkx as nx

import unittest
import mox
from moka import *
from component import Component
from item import Item

from behaviors.requirements import requirement as req
from environment import Environment

from state import State

class TestComponentInitialization(unittest.TestCase):

    def test_makes_self_component(self):
        "Freshly initialized components have no components"
        # TODO Use the descriptor protocol to do this?
        subject = Component()
        self.assertEqual(len(subject.components), 0)

class TestComponentRegistration(unittest.TestCase):

    def test_knows_its_container(self):
        """
        A component should know who contains it
        """

        a = Item()
        b = Component()
        a.register_component(b)
        self.assertEqual(b.container, a)
# TEST BEHAVIOR REGISTRATION ############################

class TestRegisterBehavior(unittest.TestCase):

    def test_should_add_to_behaviors(self):
        subject = Component()
        subject.register_behavior("Foo")
        self.assertIn(subject.behaviors, "Foo")


# TEST REQUIREMENT TESTING ##############################

class TestTestRequirements(unittest.TestCase):
    pass

class TestGenericRequirementChecking(unittest.TestCase):

    def test_requirements_single_item(self):
        """An item should be able to fulfill its own requirements"""
        pass

    def test_requirements_single_nested_item(self):
        """An item nested one layer deep should be able to fulfill requirements"""
        # TODO pending revision
        pass


    def test_should_return_list_of_requirements_unmet(self):
        pass

    def test_input_requirements_should_only_test_inputs(self):
        pass

    def test_output_requirements_should_only_test_outputs(self):
        pass

# TEST INPUT/OUTPUT REGISTRATION ####################################

class TestPlugInto(unittest.TestCase):

    def setUp(self):
        self.subject = Component()
        self.other = Component()

    def test_plug_into_creates_one_output_for_self(self):
        """
        Plugging into another should add one output to self
        and one input to the target
        """
        self.subject.plug_into(self.other)
        self.assertIsInstance(self.subject.connectivity_graph, nx.DiGraph)
        self.assertEqual(len(self.subject.item_outputs()), 1)
        self.assertEqual(len(self.other.item_inputs()), 1)

class TestPlugInto(unittest.TestCase):

    def setUp(self):
        self.subject = Component()
        self.other = Component()

    def test_plug_out_from_creates_one_input_for_self(self):
        """
        Plugging out from another should add one input to self
        and one output to the target
        """
        self.subject.plug_out_from(self.other)
        self.assertIsInstance(self.subject.connectivity_graph, nx.DiGraph)
        self.assertEqual(len(self.subject.item_inputs()), 1)
        self.assertEqual(len(self.other.item_outputs()), 1)

class TestDuplexes(unittest.TestCase):

    def test_duplexes(self):
        """
        Duplexes returns duplexed components
        """
        subject = Component()
        the_object = Component()
        other_guy = Component()

        subject.plug_into(other_guy)
        subject.establish_duplex(the_object)

        self.assertIsInstance(subject.duplexes(), List)
        self.assertEqual(len(subject.duplexes()), 1)
        self.assertEqual(subject.duplexes()[0], the_object)

## TEST INPUT/OUTPUT QUERYING

class TestInputsWithFlag(unittest.TestCase):
    pass

class TestOutputsWithFlag(unittest.TestCase):
    pass

if __name__ == "__main__":

    unittest.main()
