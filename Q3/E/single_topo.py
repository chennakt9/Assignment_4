from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
import sys
import time


net = Mininet(SingleSwitchTopo(k=6))
net.start()

h1 = net.get('h1')
p1 = h1.popen('python server_tcp.py &',stdout=sys.stdout,stderr=sys.stdout)
time.sleep(0.001)

print("lkasjdfhlas",h1.IP)
h1 = net.get('h2')
p1 = h1.popen('python 1_client_tcp.py',stdout=sys.stdout,stderr=sys.stdout)

# h2 = net.get('h2')
# h2.cmd('python myClient.py -i %s -m "hello world"' % h1.IP())

# CLI( net )
# p1.terminate()

print(net.hosts)
print(net.hosts[0])


net.pingAll()

net.stop()


