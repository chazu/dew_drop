import unittest

import sys
sys.path.append("./../")

from component import Component
from item import Item

from state import State

class TestBeahviorExecutionViaSignal(unittest.TestCase):
    pass
    # def test_send(self):
    #     """
    #     Make sure you can change state by sending a signal
    #     """
    #     door = Door()
    #     self.assertEqual(door.state.isstate('open'), False)
    #     door.send('force')
    #     self.assertEqual(door.state.isstate('open'), True)

    # def test_send_from_component(self):
    #     """
    #     Make sure behaviors which send signals actually impact target state
    #     """
    #     door = Door()
    #     self.assertEqual(door.state.isstate('open'), False)
    #     actuator = Actuator()
    #     actuator.plug_into(door)
    #     actuator.behaviors['output force'].behave(actuator)
    #     self.assertEqual(door.state.isstate('open'), True)



if __name__ == '__main__':

    unittest.main()
