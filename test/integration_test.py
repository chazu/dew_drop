import unittest

import sys
sys.path.append("./../")

from component import Component

from behaviors.exports import network
import behaviors.requirements.requirement as req

class TestGetRemoteHosts(unittest.TestCase):

    def test_get_remote_hosts_sets_empty_list(self):
        subject = Component()
        subject.execute_behavior(network.GetNetworkHosts)
        self.assertEqual(subject.state.available_hosts, [])

    def test_get_remote_hosts_sets_hosts(self):
        subject = Component()
        nic = Component()
        the_object = Component()
        the_object.state.set_flag("IS_NETWORK_HOST")
        subject.register_component(nic)
        nic.establish_duplex(the_object)
        subject.execute_behavior(network.GetNetworkHosts)
        self.assertEqual(len(subject.state.available_hosts), 1)
        self.assertIn(subject.state.available_hosts, the_object)
unittest.main()
