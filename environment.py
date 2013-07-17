class Environment(object):
    """
    Represents the environment with which a given item is capable of interacting. 
    """

    def __init__(self, env_type):
        self.env_type = env_type

    def register_variable(self, var, value):
        setattr(self, var, value)
