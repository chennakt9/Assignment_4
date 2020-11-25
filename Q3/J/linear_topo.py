from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange, dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
import sys


class LinearTopo(Topo):
    def __init__(self, k=2, bw=10, **opts):
        super(LinearTopo, self).__init__(**opts)

        self.k = k
        self.bw = bw

        first_switch = self.addSwitch('s1')

        prev_switch = first_switch
        for i in range(2, k+1):
            switch = self.addSwitch('s%s'%i)
            self.addLink(switch, prev_switch)
            prev_switch = switch
        last_switch = switch

        first_host = self.addHost('h1')
        last_host = self.addHost('h2')

        
        self.addLink(first_switch,first_host)

        self.addLink(last_switch,last_host)
        # 10 Mbps, 5ms delay, 1% loss, 1000 packet queue
        #    self.addLink( host, switch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
            

            

# for band_width in (10,100,1024):

number_of_switches = int(input("Enter Number of Switches : "))
topo = LinearTopo(k=number_of_switches,bw=1000)
net = Mininet(topo, host=CPULimitedHost, link=TCLink)
net.start()


h1 = net.get('h1')
HOST = h1.IP()
p1 = h1.popen(f'python server_tcp.py {HOST}',stdout=sys.stdout,stderr=sys.stdout)

h2 = net.get('h2')
h2.popen(f"python client_tcp.py {HOST}",stdout=sys.stdout,stderr=sys.stdout)

CLI( net )



net.stop()


