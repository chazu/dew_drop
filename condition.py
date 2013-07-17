class Condition(object):
    """
    An object representing the current condition of an item or component.

    Common to all items - 
    - Durability              -  - The amount of decay which occurs with [each] use
    - Unreliability Threshold -  - The threshold of durability at which the component becomes unreliable (output accuracy begins to decrease)
    - Operability Threshold   -  - The Threshold of durability at which the component begins to have a chance of failure
    - Failure Rate            -  - The chance of failure once the operability threshold is crossed
    - Critical Failure Chance -  - The chance of a critical failure
    - Damage spread           -  - How evenly damage is distribued throughout components
    """


    def __init__(self, owner,config_dict):

        self.owner = owner

        self.durability = config_dict['durability']
        self.original_durability = config_dict['durability']
        self.durability = config_dict['unreliable_threshold']
        self.durability = config_dict['operational_threshold']
        self.durability = config_dict['failure_rate']
        self.durability = config_dict['critical_failure_chance']
        self.durability = config_dict['damage_spread']

    def update_condition(self):
        self.durability -= 1
        if self.original_durability / float(self.durability) < self.unreliability_threshold:
            pass
            # Adjust the input and/or output error
        if self.original_durability / float(self.durability) < self.operational_threshold:
            pass
            # Roll for failure

    def check_failure(self):
        pass
        # check for failure
        # check for/handle critical failure

# Aspects of Item quality - 
#  - durability        - the amount of decay which occurs with use
#  - reliability       - the chance of failure without breakage 
#  - accuracy          - the variance in output during normal operation
#  - failure severity  - the average damage done to the item when failure does occur
#  - failure isolation - how systemic or isolated a failure is among the components of the item
 
# im noticing a pattern here - a trait has a value representing the average, and a value representing the variation from that average. 

# example: rocket engine

# has components: tank, chamber, pump assembly

# pump assembly has components - ???

# tank has components - ceramic

# chamber has components - carbon-fibre reinforced ceramic

# NOTE: ATOMIC components are those which cannot be broken down. ceramic and carbon-fibre reinforced ceramic are examples.

# On each use of the rocket engine, durability is decreased by a set amount, the durability factory.

# Once the durability surpasses the unreliability threshold, the accuracy of the output becomes less and less reliable.

# Once the operational threshold is passed, the chance of a failure becomes greater and greater with each use

# Once a failure occurs, a check is done to see how many of the components are affected, and how severely. Different factors determine the severity of the failure and the isolation of the failure with respect to the components. Critical failures result in the destruction of the item. 
#HOW DO WE FACTOR THE COMPEXITY OF AN OBJECT INTO THIS SYSTEM? E.G. WHEN A SUPERCOMPUTER BREAKS ITS GOT TO BE HARDER TO LOCATE THE ISSUE THAN WHEN A WRENCH BREAKS
# Once a failure occurs, a check is done to see how many of the components are affected, and how severely. Different factors determine the severity of the failure and the isolation of the failure with respect to the components. Critical failures result in the destruction of the item. 


# HOW DO WE FACTOR THE COMPEXITY OF AN OBJECT INTO THIS SYSTEM? E.G. WHEN A SUPERCOMPUTER BREAKS ITS GOT TO BE HARDER TO LOCATE THE ISSUE THAN WHEN A WRENCH BREAKS
