'''
Welcome to the first version of my uhv interlock simulator! This implements our uhv system using a graph data structure, and the
benefit of using this approach is that it is algorithmic by nature, making it very easily scaled up and expanded. This program is
the driver program, the other three files (three for now) are all class files that you can look at if you want to see the meat and
bones behind the implementation.

This code deals with 2 of the 4 variables considered in interlock: internal chamber pressure and neighboring valve status. There are a
few key assumptions/restrictions that go along with this:
- This version only deals with chamber-chamber valves (gv1,2,4,5,6,7,9) (pump-chamber and pump-pump valves are coming next)
- C-C valves are closed by default and only have special opening conditions (P-C and P-P valves are more complicated)
- Chamber pressure status is boolean: True is good, False is bad (we discussed piecewise boolean pressure conditions in our last meeting, that's also coming)
- Gate valve status is boolean: True is open, False is closed (pretty sure this isn't arguable)

HOW THIS WORKS
Each chamber is a node, which has 2 attributes: name (str) and status (bool). Each gate valve is an edge, which has 4 attributes: starting chamber (node),
ending chamber (node), name (str), and status (bool). I initialized all of our relevant chambers and valves in main(), but you can go nuts with however many
chambers and valves you want. uhv is instantiated as a weighted_graph object, and that gives it a bunch of cool methods:
- print(uhv): spits out the adjacency lists for every node in the form: (node that it's next to, valve connecting them, status of that valve)
- check_subgraph(edge): takes a given valve and scans the surrounding valves (i.e. looks at the caterpillar subgraph formed around the given edge) and says
whether or not it is ok to open that valve
- open_valve(edge): using check_subgraph, this will open a valve if it's ok to do so and update all relevant fields, if it's not ok, it will not close it and
instead tell you what is preventing it from closing (which valves are open and which chamber is bad)
- close_valve(edge): closes a valve and updates relevant fields

You can write a bunch of different commands to simulate opening and closing valves to create a path, and it will reset everytime you run the program again.
Please let me know what you think!
'''

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
