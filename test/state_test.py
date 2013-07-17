import unittest

import sys
sys.path.append("./../")

from component import Component
from item import Item

from state import State, StateType


class TestStateTypeClass(unittest.TestCase):

    def test_create(self):
        "Test state creation"
        subject = StateType('foo',{'initial':'bar'})
        self.assertIsInstance(subject, StateType)

class TestStateClass(unittest.TestCase):

    def test_create_blank_state_machine(self):
        "You should be able to create a blank state"
        subject = State()
        self.assertIsInstance( subject, State )
        self.assertEqual( subject.flags, [] )
        self.assertEqual( subject.states, {} )

    def test_add_state_machine(self):
        "Adding a state type"
        test_state_type = StateType('foo',{'initial':'bar'})
        subject = State(test_state_type)


    def test_includes(self):
        """pythonic syntax for testing whether a certain type of state
        is tracked"""
        test_state_type = StateType('foo',{'initial':'bar'})
        subject = State(test_state_type)
        self.assertEqual('foo' in subject, True)
        self.assertEqual('bar' in subject, False)

    def test_set_flag(self):
        subject = State()
        subject.set_flag('IS_OPENABLE')
        self.assertTrue('IS_OPENABLE' in subject.flags)

    def test_get_flag(self):
        subject = State()
        subject.set_flag('IS_OPENABLE')
        self.assertTrue(subject.has_flag('IS_OPENABLE'))

    def test_owner_true(self):
        """A state should know who owns it"""
        subject = State()
        pass

    def test_set_variable(self):
        "Set attributes for a component"
        subject = State()
        subject.set_variable('foo', 1)
        self.assertEqual(subject.foo, 1)

    def test_set_variable_default_value(self):
        "Attributes for a component default to None"
        subject = State()
        subject.set_variable('foo')
        self.assertEqual(subject.foo, None)

if __name__ == "__main__":
    unittest.main()

