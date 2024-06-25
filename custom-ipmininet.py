from ipmininet.iptopo import IPTopo
from ipmininet.router.config import RouterConfig

class MyTopo( IPTopo ):
    
    def build(self, *args, **kwargs):
        # Create hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
 
        # Create router
        r1 = self.addRouter('r1')
 
        # Add links between the switch and each host
        lr1h1 = self.addLink(r1, h1)
        lr1h1[h1].addParams(ip=("10.0.0.1/24"))
        lr1h1[r1].addParams(ip=("10.0.0.2/24"))
        
        lr1h2 = self.addLink(r1, h2)
        lr1h2[h2].addParams(ip=("10.0.1.1/24"))
        lr1h2[r1].addParams(ip=("10.0.1.2/24"))
        
        super().build(*args, **kwargs)
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
