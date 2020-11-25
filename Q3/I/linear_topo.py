from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
import sys

class LinearTopo(Topo):
   "Linear topology of k switches, with one host per switch."

   def __init__(self, k=2,bw = 10,loss=1, **opts):
       """Init.
           k: number of switches (and hosts)
           hconf: host configuration options
           lconf: link configuration options"""

       super(LinearTopo, self).__init__(**opts)

       self.k = k
       self.bw = bw
       self.loss = loss
    
       switch = self.addSwitch('s1')

       for i in range(1, k+1):
           host = self.addHost('h%s' % i)
           

           self.addLink( host, switch, bw = self.bw,loss=self.loss)
           # 10 Mbps, 5ms delay, 1% loss, 1000 packet queue
        #    self.addLink( host, switch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
            

            

# for band_width in (10,100,1024):

loss_percent = int(input("Enter loss % : "))
topo = LinearTopo(k=2,bw=1000,loss=loss_percent)
net = Mininet(topo, host=CPULimitedHost, link=TCLink)
net.start()

h1 = net.get('h1')
HOST = h1.IP()
p1 = h1.popen(f'python server_tcp.py {HOST}',stdout=sys.stdout,stderr=sys.stdout)

h2 = net.get('h2')
h2.popen(f"python client_tcp.py {HOST}",stdout=sys.stdout,stderr=sys.stdout)


CLI( net )


net.stop()


