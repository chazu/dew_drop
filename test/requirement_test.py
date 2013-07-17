import unittest
import mox
import sys
sys.path.append("./../")

import behaviors.requirements.requirement as req
from component import Component

class TestComponentsFilteredForFlag(unittest.TestCase):

    def test_it_filters(self):
        """
        It should filter out all components which
        do not have the specified flag
        """
        subject = Component()
        subject.register_component(Component())
        subject.register_component(Component())
        sub_subject = Component()
        sub_subject.state.set_flag('HEY')
        subject.register_component(sub_subject)
        self.assertEqual(len(req.components_filtered_for_flag(subject, 'HEY')), 1)


class TestComponentsOf(unittest.TestCase):

    def test_should_return_components_of_component(self):
        """
        Should return components of component passed in
        """
        subject = Component()
        subject.register_component('doo')
        subject.register_component('pee')

        self.assertEqual(req.components_of(subject)[0],'doo')

    def test_should_return_empty_list(self):
        """
        Should return empty list if no components registered
        """
        subject = Component()

        self.assertEqual(req.components_of(subject), [])


class TestComponentsOfList(unittest.TestCase):

    def test_should_return_empty_list(self):
        """
        Should contain empty list if no components registered
        """
        subject = Component()

        self.assertEqual(req.components_of_list(subject.components), [])

    def test_should_return_list_of_lists(self):
        """
        Should return list of lists if components registered
        """
        subject = Component()
        subject.register_component(Component())
        self.assertEqual(req.components_of_list(subject.components), [[]])

    def test_should_return_list_of_lists_containing_components(self):
        """
        Should return list of lists with components in them
        if components registered
        """
        subject = Component()
        sub_subject = Component()
        returned_component = Component()
        sub_subject.register_component(returned_component)
        subject.register_component(sub_subject)
        self.assertEqual(req.components_of_list(subject.components), [[returned_component]])


class TestTestComponentInputs(unittest.TestCase):

    def test_test_component_inputs_failure(self):
        "test_component_inputs should return false if an unmet input requirement exists"
        the_input = Component()
        the_input.state.set_flag('BAR')
        requirement = lambda x: 'FOO' in x.state.flags
        subject = Component()
        self.assertIsInstance(the_input, Component)
        subject.plug_out_from(the_input)
        subject.register_component(the_input)

        self.assertFalse(req.test_component_inputs(the_input, requirement))

    def test_test_component_inputs_pass(self):
        """test_component_inputs should return True if
        all input requirements are met"""
        requirement = lambda component : 'IS_FOO' in component.state.flags
        subject = Component()
        the_input = Component()
        the_input.state.set_flag('IS_FOO')
        subject.register_component(the_input)
        the_input.plug_into(subject)
        self.assertEqual(len(subject.item_inputs()), 1)
        self.assertEqual(req.test_component_inputs(subject, requirement), True)


class TestTestComponentOutputs(unittest.TestCase):

    def test_test_component_outputs_failure(self):
        """test_component_outputs should return false if
        an unmet output requirement exists"""
        requirement = lambda component : 'IS_BAR' in component.state.flags
        subject = Component()
        the_output = Component()
        the_output.state.set_flag('IS_FOO')
        subject.plug_into(the_output)
        self.assertEqual(bool(req.test_component_outputs(subject, requirement)), False)

    def test_test_component_outputs_pass(self):
        """test_component_outputs should return True if
        all output requirements are met"""
        requirement = lambda component : 'IS_FOO' in component.state.flags
        subject = Component()
        the_output = Component()
        the_output.state.set_flag('IS_FOO')
        subject.register_component(the_output)
        the_output.plug_out_from(subject)
        self.assertEqual(len(subject.item_outputs()), 1)
        self.assertEqual(req.test_component_outputs(subject, requirement), True)


if __name__ == "__main__":

    unittest.main()
