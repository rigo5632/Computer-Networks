#! /usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.node import OVSController

class part1_topo(Topo):    
    def build(self):
        # switches
        switch1 = self.addSwitch('s1')

        # hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')

        # links
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch1)
        self.addLink(host4, switch1)

topos = {'part1' : part1_topo}

if __name__ == '__main__':
    t = part1_topo()
    net = Mininet (topo=t, controller=OVSController)
    net.start()
    CLI(net)
    net.stop()
