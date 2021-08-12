from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' ) 
	h2 = self.addHost( 'h2' ) 
	h3 = self.addHost( 'h3' ) 
	h4 = self.addHost( 'h4' ) 
	h5 = self.addHost( 'h5' ) 
	h6 = self.addHost( 'h6' ) 
	h7 = self.addHost( 'h7' ) 
	h8 = self.addHost( 'h8' ) 
	h9 = self.addHost( 'h9' ) 
	h10 = self.addHost( 'h10' ) 
	h11 = self.addHost( 'h11' ) 
	h12 = self.addHost( 'h12' ) 
	h13 = self.addHost( 'h13' ) 
	h14 = self.addHost( 'h14' ) 
	h15 = self.addHost( 'h15' ) 
	h16 = self.addHost( 'h16' ) 
	h17 = self.addHost( 'h17' ) 
	h18 = self.addHost( 'h18' ) 
	h19 = self.addHost( 'h19' ) 
	h20 = self.addHost( 'h20' ) 
	h21 = self.addHost( 'h21' ) 
	h22 = self.addHost( 'h22' ) 
	h23 = self.addHost( 'h23' ) 
	h24 = self.addHost( 'h24' ) 
	h25 = self.addHost( 'h25' ) 
	h26 = self.addHost( 'h26' )
	s1 = self.addSwitch( 's1' ) 
	s2 = self.addSwitch( 's2' ) 
	s3 = self.addSwitch( 's3' ) 
	s4 = self.addSwitch( 's4' ) 
	s5 = self.addSwitch( 's5' ) 
	s6 = self.addSwitch( 's6' ) 
	s7 = self.addSwitch( 's7' ) 
	s8 = self.addSwitch( 's8' )

	# Add links

	self.addLink( 's1', 's7' )
	self.addLink( 's2', 's7' )
	self.addLink( 's3', 's7' )
	self.addLink( 's4', 's7' )
	self.addLink( 's5', 's7' )
	self.addLink( 's6', 's7' )
	self.addLink( 's1', 's8' )
	self.addLink( 's2', 's8' )
	self.addLink( 's3', 's8' )
	self.addLink( 's4', 's8' )
	self.addLink( 's5', 's8' )
	self.addLink( 's6', 's8' )
	self.addLink( 'h1', 's1' )
	self.addLink( 'h2', 's1' )
	self.addLink( 'h3', 's1' )
	self.addLink( 'h4', 's1' )
	self.addLink( 'h5', 's1' )
	self.addLink( 'h6', 's1' )
	self.addLink( 'h7', 's2' )
	self.addLink( 'h8', 's2' )
	self.addLink( 'h9', 's3' )
	self.addLink( 'h10', 's3' )
	self.addLink( 'h11', 's4' )
	self.addLink( 'h12', 's4' )
	self.addLink( 'h13', 's5' )
	self.addLink( 'h14', 's5' )
	self.addLink( 'h15', 's6' )
	self.addLink( 'h16', 's6' )
	self.addLink( 'h17', 's2' )
	self.addLink( 'h18', 's2' )
	self.addLink( 'h19', 's3' )
	self.addLink( 'h20', 's3' )
	self.addLink( 'h21', 's4' )
	self.addLink( 'h22', 's4' )
	self.addLink( 'h23', 's5' )
	self.addLink( 'h24', 's5' )
	self.addLink( 'h25', 's6' )
	self.addLink( 'h26', 's6' )

topos = { 'mytopo': ( lambda: MyTopo() ) }

