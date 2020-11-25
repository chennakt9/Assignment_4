from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
import sys



net = Mininet(SingleSwitchTopo(k=6))
net.start()

h1 = net.get('h1')
HOST = h1.IP()
p1 = h1.popen(f'python server_tcp.py {HOST}',stdout=sys.stdout,stderr=sys.stdout)


files = ["1_client_tcp.py","2_client_tcp.py","3_client_tcp.py","4_client_tcp.py","5_client_tcp.py"]


for h,file in list(zip(net.hosts[1:],files)):
    h.popen(f"python {file} {HOST}",stdout=sys.stdout,stderr=sys.stdout)


CLI( net )


net.stop()


