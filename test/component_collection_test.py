import sys
sys.path.append("./../")

import unittest

from component import Component
from component_collection import ComponentCollection

class TestIsEmpty(unittest.TestCase):

    def test_should_be_truthy(self):
        subject = ComponentCollection()
        self.assertTrue(subject.is_empty())

    def test_should_be_falsy(self):
        subject = ComponentCollection()
        subject.append(Component())
        self.assertFalse(subject.is_empty())

class RecursivelyCollectComponents(unittest.TestCase):

    def test_should_return_component_collection(self):
        """
        Should return instance of ComponentCollection
        """
        subject = ComponentCollection()
        self.assertIsInstance(subject.recursively_collect_components(), ComponentCollection)

    def test_should_return_empty(self):
        """
        Should return empty collection if no components
        """
        subject = ComponentCollection()
        self.assertTrue(subject.recursively_collect_components().is_empty)

    def test_should_return_components(self):
        """
        Should return all components from a collection
        in which components have no nested components
        """

        subject = ComponentCollection()
        widget, doodad = Component(), Component()
        subject.append(widget); subject.append(doodad)
        self.assertEqual(len(subject.data), 2)

    def test_should_return_nested_components(self):
        """
        Should return all components including components
        of components
        """
        subject = ComponentCollection()
        widget = Component()
        doodad = Component()
        widget.components.append(doodad)
        subject.append(widget)

        self.assertFalse(subject.is_empty())
        self.assertIn(widget, subject.recursively_collect_components())
        self.assertIn(doodad, subject.recursively_collect_components())

    def test_should_return_arbitrarily_nested_components(self):
        """
        Should return components nested more than
        one layer deep
        """
        subject = ComponentCollection()
        widget = Component()
        widget.name = "widget"
        doodad = Component()
        doodad.name = "doodad"
        whatsit = Component()
        whatsit.name = "whatsit"
        widget.components.append(doodad)
        doodad.components.append(whatsit)
        subject.append(widget)

        self.assertIn(whatsit, subject.recursively_collect_components())

    # def test_should_return_arbitrarily_nested_item_inputs(self):
    #     """
    #     Should also work for item inputs
    #     """

    #     subject = ComponentCollection()
    #     widget = Component()
    #     widget.name = "widget"
    #     doodad = Component()
    #     doodad.name = "doodad"
    #     whatsit = Component()
    #     whatsit.name = "whatsit"

    #     widget.item_inputs.append(doodad)
    #     doodad.item_inputs.append(whatsit)
    #     subject.append(widget)

    #     self.assertEqual(len(subject.data), 1)
    #     self.assertEqual(len(subject.data[0].components), 0)
    #     self.assertEqual(len(subject.data[0].item_inputs), 1)
    #     self.assertEqual(len(subject.data[0].item_inputs.data), 1)
    #     self.assertEqual(subject.data[0], widget)
    #     self.assertEqual(subject.data[0].item_inputs.data[0], doodad)
    #     self.assertEqual(subject.data[0].item_inputs.data[0].item_inputs.data[0], whatsit)
    #     self.assertEqual(len(subject.recursively_collect_components('item_inputs')), 3)
    #     self.assertIn(widget, subject.recursively_collect_components('item_inputs'))
    #     self.assertIn(doodad, subject.recursively_collect_components('item_inputs'))
    #     self.assertIn(whatsit, subject.recursively_collect_components('item_inputs'))

class TestDuplexes(unittest.TestCase):
    pass

class TestAppend(unittest.TestCase):

    def test_should_add_thing_passed_in(self):
        subject = ComponentCollection()
        self.assertEqual(len(subject.data), 0)
        subject.append("foo")
        self.assertEqual(len(subject.data), 1)
        self.assertEqual(subject.data[0], "foo")

    def test_should_have_unique_collection(self):
        subject = ComponentCollection()
        other = ComponentCollection()
        subject.append("foo")
        self.assertEqual(False, "foo" in other.data)

if __name__ == "__main__":
    unittest.main()
