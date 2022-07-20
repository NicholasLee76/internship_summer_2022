from node import Chamber
from node import Turbo
from node import Cryo
from edge import Edge
from arm import Arm

gb = Chamber('gb', 760)
ld = Chamber('ld', 10 ** -9)
bus = Chamber('bus', 10 ** -10)
ombe = Chamber('ombe', 10 ** -10)
mmbe = Chamber('mmbe', 10 ** -10)
smi = Chamber('smi', 10 ** -10)
upper = Chamber('upper', 10 ** -10)
lower = Chamber('lower', 10 ** -10)
backup = Chamber('backup', 10 ** -7)

scroll = Turbo('scroll', 1500)
hp1200 = Turbo('hp1200', 1500)
hp80_1 = Turbo('hp80_1', 1500)
hp300m_1 = Turbo('hp300m_1', 1500)
hp700_1 = Turbo('hp700_1', 1500)
hp700_2 = Turbo('hp700_2', 1500)
hp700_3 = Turbo('hp700_3', 1500)
hp80_3 = Turbo('hp80_3', 1500)
cryo = Cryo('cryo', 50)

v1 = Edge(gb, scroll, 'v1', True)
v2 = Edge(hp80_1, ld, 'v2', True)
v3 = Edge(backup, hp700_1, 'v3', True)
v4 = Edge(backup, hp300m_1, 'v4', True)
v5 = Edge(backup, hp700_3, 'v5', True)
v6 = Edge(backup, cryo, 'v6', True)
v7 = Edge(backup, hp700_1, 'v7', True)
v8 = Edge(backup, hp80_3, 'v8', True)
gv1 = Edge(gb, ld, 'gv1', False)
gv2 = Edge(ld, ombe, 'gv2', False)
gv3 = Edge(hp1200, ombe, 'gv3', False)
gv4 = Edge(ld, bus, 'gv4', False)
gv5 = Edge(bus, smi, 'gv5', False)
gv6 = Edge(bus, mmbe, 'gv6', False)
gv7 = Edge(bus, upper, 'gv7', False)
gv8 = Edge(hp300m_1, upper, 'gv8', True)
gv9 = Edge(upper, lower, 'gv9', False)  # gv10 is helium lamp, we'll figure that out later
gv11 = Edge(hp700_3, lower, 'gv11', True)
gv12 = Edge(cryo, lower, 'gv12', False)
gv13 = Edge(hp700_2, smi, 'gv13', True)
gv14 = Edge(hp700_1, mmbe, 'gv14', True)

ta1 = Arm('ta1', gv4, False)
ta2 = Arm('ta2', gv7, False)
ta3 = Arm('ta3', gv6, False)
ta4 = Arm('ta4', gv5, False)
mn = Arm('mn', gv9, False)

chambers = [gb, ld, bus, ombe, mmbe, smi, upper, lower, backup]
pumps = [scroll, hp1200, hp80_1, hp300m_1, hp700_1, hp700_2, hp700_3, cryo]
valves = [v1, v2, v3, v4, v5, v6, v7, v8, gv1, gv2, gv3, gv4, gv5, gv6, gv7, gv8, gv9, gv11, gv12, gv13, gv14]
arms = [ta1, ta2, ta3, ta4, mn]
