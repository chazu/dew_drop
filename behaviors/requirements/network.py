from requirement import *

def is_network_host(component, **kwargs):
    return component.state.specifies["is_network_host"]

def has_physical_link_to_host(component, **kwargs):
    return "Not implemented"
