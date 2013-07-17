from requirement import *

def has_network_link(component, **kwargs):
    return not component.components.with_flag('IS_NETWORK_LINK').is_empty()

def has_physical_link_to_host(component, **kwargs):
    return "Not implemented"
