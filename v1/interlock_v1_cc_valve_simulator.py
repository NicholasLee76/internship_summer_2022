from node import Node
from edge import Edge
from weighted_graph import Weighted_Graph

def main():
    gb = Node('gb', True)
    ld = Node('ld', True)
    bus = Node('bus', True)
    ombe = Node('ombe', True)
    mmbe = Node('mmbe', True)
    smi = Node('smi', True)
    upper = Node('upper', True)
    lower = Node('lower', True)

    gv1 = Edge(gb, ld, 'gv1', False)
    gv2 = Edge(ld, ombe, 'gv2', False)
    gv4 = Edge(ld, bus, 'gv4', False)
    gv5 = Edge(bus, smi, 'gv5', False)
    gv6 = Edge(bus, mmbe, 'gv6', False)
    gv7 = Edge(bus, upper, 'gv7', False)
    gv9 = Edge(upper, lower, 'gv9', False)

    nodes = [gb, ld, bus, ombe, mmbe, smi, upper, lower]
    edges = [gv1, gv2, gv4, gv5, gv6, gv7, gv9]
    uhv = Weighted_Graph(nodes, edges)

    print(uhv)

if __name__ == '__main__':
    main()
