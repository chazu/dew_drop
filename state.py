import logging
from copy import copy

from util import *

logging.basicConfig(level=logging.DEBUG)

class State(object):

    def __init__(self, spec=None):
        self.flags = []
        self.spec  = spec if spec else {}
        self.current_state = copy(self.spec)

    def __getitem__(self, key):
        return self.spec[key]

    def __setitem__(self, key, value):
        self.spec[key] = value

    def merge_state(self, path_list, state_hash):
        """
        For use during behavior registration -
        Adds state to self.current_state
        """
        res = multiIndex(self.current_state, path_list)
        res = state_hash

    def specifies(self, key, value=None, path=None):
        """
        Key - The key to search for
        Value - A value to check equality for
        Path - The path in the spec to search

        True if the spec doc has the key.
        If value is passed in, True only
        if key is present and equal to value
        """
        try:
            if path != None and isDict(multiIndex(self.current_state, path)):
                target = multiIndex(self.current_state, path)
                logging.debug("Specification found: ")
                logging.debug("Key   : " + key)
                logging.debug("path  : " + str(path))
                logging.debug("value: " + str(target))
                return key in target.keys()
            else:
                target = self.current_state
                logging.debug("Specification found: ")
                logging.debug("Key         : " + key)
                logging.debug("equals value: " + str(value))
                logging.debug("at spec path: " + str(path))
                return key in target.keys() and (
                    target[key] == value if value != None else True)
        except KeyError:
            logging.debug("WARNING: Key error when requesting path " + \
                str(path) + " for widget " + self.name)

    def specifies_not_equal(self, key, value):
        """
        True if the value is specified but not equal to given value
        """
        return self.current_state[key] != value

    def report(self):
        pass
