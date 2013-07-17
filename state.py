from fysom import Fysom

# TODO Set up a default state machine

class StateType():

    def __init__(self, name, config_dict={}):
        self.name = name
        self.owner = None
        self.behaviors = []

    def set_variable(self, var, value=None):
        self.__dict__[var] = value

    def set_owner(self, owner):
        self.owner = owner
        for behavior in self.behaviors:
            self.owner.register_behavior(behavior)

    def unset_owner(self):
        for behavior in self.behaviors:
            self.owner.unregister_behavior(behavior)


class State(object):

    def __init__(self, *args):
        self.flags = []
        self.states = {}
        if len(args) > 0:
            if len(args) > 0:
                for state_type in args:
                    self.states[state_type.name] = state_type

    def add_state_type(self, state_type):
        for state_type in self.states:
            self.states[state_type.name] = state_type()

    def set_flag(self, flag):
        self.flags.append(flag)

    def has_flag(self, flag):
        return flag in self.flags

    def set_variable(self, var, value=None):
        self.__dict__[var] = value

    def has_variable(self, flag):
        return flag in self.__dict__

    def __contains__(self, state_type_name):
        return state_type_name in self.states

    def __getattr__(self, attribute):
        return None

    def report(self):
        print("+++++++++")
        print("+ FLAGS +")
        print("+++++++++")
        print(self.flags)
        print("++++++++")
        print("+ VARS +")
        print("++++++++")
        print(self.__dict__)

# STATE LIBRARY ##################################
