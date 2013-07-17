import itertools

# TODO reorganize requirements module for @#@# sake

################
#UTIL FUNCTIONS#
################

def components_filtered_for_flag(component, flag):
    if len(component.components) > 0:
        return [ component for component in component.components \
                     if component.state.has_flag(flag) ]
    else:
        return []

def components_of(component):
    "Return all components of the component passed in"
    return component.components.data

def components_of_list(component_list):
    "Return a list of component lists"
    return [ components_of(component) for component in component_list ]

def recursively_test_component(component, requirement):
    if requirement(component) == True:
        return True
    else:
        if len(component.components) == 0:
            return False
        else:
            for component in component.components:
                recursively_test_component(component, requirement)

def test_component_inputs(component, requirement):
    for the_input in component.item_inputs():
            if requirement(the_input) == True:
                return True
    return False # If not returned yet, must have failed

def test_component_outputs(component, requirement):
    for the_output in component.item_outputs():
            if requirement(the_output) == True:
                return True
    return False # If not returned yet, must have failed
