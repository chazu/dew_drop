import sys
import os

clear = lambda: os.system('clear')

sys.path.append("./../")
sys.path.append("./../../")

import urwid
from widgets.menu import SimpleMenu
from widgets.context import UIContext, ContextAwareLoop

# Import All your Behaviors
from behavior_editor import BehaviorEditorApp

from component import Component

from malcolm.base import get_manufacturer_name

# SAVIN' AND LOADIN'
import shelve

class App():

    def __init__(self):
        self.current_item = None

    def initialize_dependencies(self, save_path):
        self.save_path = save_path
        # Make sure the directory for pickling items is there
        # Load all behaviors

    def main_menu(self):
        self.list_all_items()
        if self.current_item:
            self.inspect_current_item()
        print "==============================================="
        print "ITEM EDITOR"
        print "CURRENTLY EDITING: " + self.current_item.name if self.current_item else "<NONE>"
        print "1) ADD NEW ITEM"
        print "2) REGISTER COMPONENT"
        print "3) ADD INPUT"
        print "4) ADD OUTPUT"
        print "5) CHANGE NAME"
        print "6) SELECT NEW ITEM FOR EDITING"
        print "7) EDIT BEHAVIORS FOR ITEM"
        print "8) SAVE THIS ITEM"
        print "9) LOAD ITEM FILE"

    def add_new_item(self):
        Component(name=get_manufacturer_name())
        clear()

    def list_all_items(self):
        clear()
        for item in Component.component_register:
            print str(Component.component_register.index(item)) + ") " + item.name

    def register_component(self):
        print "input(num)ber of component to add to " + self.current_item.name
        num = input('')
        self.current_item.register_component(Component.component_register[int(num)])

    def add_input(self):
        print "num = input number of component to add as input for " + self.current_item.name
        num = input('')
        self.current_item.plug_out_from(Component.component_register[int(num)])

    def add_output(self):
        print "num = input number of component to add as output for " + self.current_item.name
        num = input('')
        self.current_item.plug_into(Component.component_register[int(num)])

    def inspect_current_item(self):
        self.current_item.report()

    def select_new_item_for_editing(self):
        print "==========================="
        print "num = input number of component to edit"
        num = input('')
        self.current_item = Component.component_register[int(num)]

    def change_name(self):
        new_name = raw_input("Enter new name: ")
        self.current_item.name = new_name

    def save_this_item(self):
        filename = raw_input("Filename: ")# Ask for filename
        d = shelve.open(filename)
        for component in Component.component_register:
            d[component.name] = component
        d.close()

    def load_item_file(self):
        # enter filename
        filename = raw_input("Filename: ")
        # load instances from shelve, add them to registry in Component class
        items = shelve.open(filename, "r")
        for key in items.keys():
            Component.component_register.append(items[key])
        print("items: ", str(items))
        num = raw_input('')

    def edit_behaviors(self):
        app = BehaviorEditorApp(self.current_item)
        app.run()

    def run(self):
        while True:
            try:
                self.main_menu()
                num = input('')
                num = int(num)
                if num == 1:
                    self.add_new_item()
                elif num == 2:
                    self.register_component()
                elif num == 3:
                    self.add_input()
                elif num == 4:
                    self.add_output()
                elif num == 5:
                    self.change_name()
                elif num == 6:
                    self.select_new_item_for_editing()
                elif num == 7:
                    self.edit_behaviors()
                elif num == 8:
                    self.save_this_item()
                elif num == 9:
                    self.load_item_file()

            except Exception, e:
                e = e
                print e
                foo = raw_input('')
app = App()

app.run()
