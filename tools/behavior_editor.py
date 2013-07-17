import traceback

import sys
import os
sys.path.append("./../")
sys.path.append("./../../")

clear = lambda: os.system('clear')

from behaviors.base import Behavior
from behaviors.exports import network

class BehaviorEditorApp():
    def __init__(self, current_item):
        self.behaviors = Behavior.__subclasses__()
        self.current_item = current_item

    def main_menu(self):
        clear()
        print("EDITING BEHAVIORS FOR :", self.current_item.name)
        print("STATE============================")
        self.current_item.report()
        self.current_item.state.report()
        print("1) Add behavior")
        print("2) Test Behavior")
        print("3) Test Requirements")
        print("4) List all behaviors")
        print("5) Add state flag")
        print("0) Quit")

    def test_behavior(self):
        print self.current_item.behaviors
        num = int(raw_input("Enter index of behavior to execute"))
        behavior = self.current_item.behaviors[num]
        self.current_item.execute_behavior(behavior)
        num = raw_input('')

    def test_requirements(self):
        print self.current_item.behaviors
        num = int(raw_input("Enter index of behavior with requirements to test: "))
        # TODO Test inupt and output as well as base requirements
        requirements = self.current_item.behaviors[num].requirements
        for requirement in requirements:
            print str(requirement) + " result: "
            print requirement(self.current_item)
        num = raw_input('PRESS ANY KEY TO CONTINUE...')

    def list_all_behaviors(self):
        for item in self.behaviors:
            print item.name
            # print(str(index), item)

    def add_behavior(self):
        clear()
        self.list_all_behaviors()
        num = raw_input("Enter number of behavior to attach");
        self.current_item.register_behavior(self.behaviors[int(num)])
        pass

    def add_state_flag(self):
        flag = raw_input("Enter flag to set: ")
        self.current_item.state.set_flag(flag)

    def run(self):
        while True:
            try:
                self.main_menu()
                num = raw_input('')
                num = int(num)
                if num == 1:
                    self.add_behavior()
                elif num == 2:
                    self.test_behavior()
                elif num == 3:
                    self.test_requirements()
                elif num == 4:
                    self.list_all_behaviors()
                elif num == 5:
                    self.add_state_flag()
                else:
                    break
            except Exception, e:
                e = e
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print "UNEXPECTED EXCEPTION: ", e
                traceback.print_tb(exc_traceback)
                num = raw_input('')
