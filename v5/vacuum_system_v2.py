from node import Chamber
from node import Pump
from node import Turbo
from node import Cryo


class VacuumSystem:
    def __init__(self, chambers, pumps, valves, arms):
        self.chambers = chambers
        self.pumps = pumps
        self.valves = valves
        self.arms = arms

        self.p_adj_dict = {node: [] for node in chambers}
        self.c_adj_dict = {node: [] for node in chambers}
        self.arm_dict = {arm.get_through_valve(): arm for arm in arms}
        self.fault_tracker = {node: [] for node in pumps}

        for valve in self.valves:
            if isinstance(valve.get_src(), Chamber) and isinstance(valve.get_dest(), Chamber):
                prev = self.c_adj_dict[valve.get_src()]
                temp = [valve.get_dest(), valve.get_name(), valve.get_weight()]
                prev.append(temp)
                self.c_adj_dict.update({valve.get_src(): prev})

                prev = self.c_adj_dict[valve.get_dest()]
                temp = [valve.get_src(), valve.get_name(), valve.get_weight()]
                prev.append(temp)
                self.c_adj_dict.update({valve.get_dest(): prev})

            elif isinstance(valve.get_src(), Chamber):
                prev = self.p_adj_dict[valve.get_src()]
                temp = [valve.get_dest(), valve.get_name(), valve.get_weight()]
                prev.append(temp)
                self.p_adj_dict.update({valve.get_src(): prev})

                prev = self.fault_tracker[valve.get_dest()]
                prev.append(valve)
                self.fault_tracker.update({valve.get_dest(): prev})

            elif isinstance(valve.get_dest(), Chamber):
                prev = self.p_adj_dict[valve.get_dest()]
                temp = [valve.get_src(), valve.get_name(), valve.get_weight()]
                prev.append(temp)
                self.p_adj_dict.update({valve.get_dest(): prev})

                prev = self.fault_tracker[valve.get_src()]
                prev.append(valve)
                self.fault_tracker.update({valve.get_src(): prev})

    def __str__(self):
        # prints adjacency lists for each chamber, including connecting edge
        ret = ""
        for key in self.c_adj_dict:
            ret += (key.get_name() + ": ")
            for item in self.c_adj_dict[key] + self.p_adj_dict[key]:
                name = item[0]
                adj_edge = item[1]
                edge_weight = item[2]
                ret += f"({name}, {adj_edge}, {edge_weight}) "
            ret += "\n"
        return ret

    def check_chambers(self, edge):
        # gets list of adjacent subgraph edges excluding given edge
        n1 = edge.get_src()
        n2 = edge.get_dest()
        adj_list1 = self.c_adj_dict[n1].copy()
        adj_list2 = self.c_adj_dict[n2].copy()
        for i, ele in enumerate(adj_list1):
            if ele[0] == n2:
                adj_list1.pop(i)
                break
        for i, ele in enumerate(adj_list2):
            if ele[0] == n1:
                adj_list2.pop(i)
                break
        edge_list = adj_list1 + adj_list2
        # checks edges and src dest nodes
        sum = 0
        bad_edges = []
        node_match = True

        for ele in edge_list:
            if ele[2]:
                sum += 1
                bad_edges.append(ele[1])
        if edge.get_src().get_data() != edge.get_dest().get_data():
            sum += 1
            node_match = False

        if sum == 0 and not edge.get_weight():
            return [True, f"{edge} can be opened"]
        elif sum == 0 and edge.get_weight():
            return [True, f"{edge} is already open"]
        else:
            return [False, bad_edges, node_match]

    def check_pump(self, edge, op):  # op is bool (T to open, F to close)
        n1 = edge.get_src()
        n2 = edge.get_dest()
        ret = [True, '']
        if op:
            if isinstance(n1, Pump):
                if isinstance(n1, Turbo):
                    if n1.get_status() and n2.get_data() == 'ultra high vacuum':
                        ret[1] += f"{edge.get_name()} is now open"
                    else:
                        if not n1.get_status():
                            ret[0] = False
                            ret[1] += f"{n1.get_name()} is not running"
                        if n2.get_data() != 'ultra high vacuum':
                            ret[0] = False
                            ret[1] += f"\n{n2.get_name()} is not ultra high vacuum"
                elif isinstance(n1, Cryo):
                    adj_list = self.c_adj_dict[n2].copy()
                    sum = 0
                    bad_edges = []
                    for ele in adj_list:
                        if ele[2]:
                            sum += 1
                            bad_edges.append(ele[1])
                    if sum != 0:
                        ret[0] = False
                        ret[1] = bad_edges
                    if n2.get_data() != "ultra high vacuum":
                        ret[0] = False
                        bad_edges.append(f"{n2.get_name()} is not ultra high vacuum")
                        ret[1] = bad_edges
                    elif sum == 0 and n2.get_data() == "ultra high vacuum":
                        ret[1] += f"{edge.get_name()} is now open"
            else:
                if isinstance(n2, Turbo):
                    if n2.get_status() and n1.get_data() == 'ultra high vacuum':
                        ret[1] += f"{edge.get_name()} is now open"
                    else:
                        if not n2.get_status():
                            ret[0] = False
                            ret[1] += f"{n2.get_name()} is not running"
                        if n1.get_data() != 'ultra high vacuum':
                            ret[0] = False
                            ret[1] += f"\n{n1.get_name()} is not ultra high vacuum"
                elif isinstance(n2, Cryo):
                    adj_list = self.c_adj_dict[n1].copy()
                    sum = 0
                    bad_edges = []
                    for ele in adj_list:
                        if ele[2]:
                            sum += 1
                            bad_edges.append(ele[1])
                    if sum != 0:
                        ret[0] = False
                        ret[1] = bad_edges
                    if n2.get_data() != "ultra high vacuum":
                        ret[0] = False
                        bad_edges.append(f"{n1.get_name()} is not ultra high vacuum")
                        ret[1] = bad_edges
                    elif sum == 0 and n1.get_data() == "ultra high vacuum":
                        ret[1] += f"{edge.get_name()} is now open"
        else:
            if isinstance(n1, Turbo):
                if not n1.get_status():
                    ret[1] += f"{edge.get_name()} is now closed"
                else:
                    ret[0] = False
                    ret[1] += f"{n1.get_name()} is running"
            elif isinstance(n1, Cryo):
                ret[1] += f"{edge.get_name()} is now closed"
            elif isinstance(n2, Turbo):
                if not n2.get_status():
                    ret[1] += f"{edge.get_name()} is now closed"
                else:
                    ret[0] = False
                    ret[1] += f"{n2.get_name()} is running"
            elif isinstance(n2, Cryo):
                ret[1] += f"{edge.get_name()} is now closed"
        return ret

    def open_valve(self, edge):
        name = edge.get_name()
        if isinstance(edge.get_src(), Chamber) and isinstance(edge.get_dest(), Chamber):
            check = self.check_chambers(edge)
            if check[0]:
                edge.set_weight(True)
                for key in self.c_adj_dict:  # fix this lmao so it doesnt need to run a double for loop every time it opens a valve
                    for i in range(len(self.c_adj_dict[key])):
                        if self.c_adj_dict[key][i][1] == edge.get_name():
                            self.c_adj_dict[key][i][2] = True
                print(f"{name} is now open")
            else:
                print(f"{name} cannot be opened:")
                for bad_edge in check[1]:
                    print(f"{bad_edge} is open\n")
                if not check[2]:
                    print("chamber pressures do not match")
        elif edge.get_weight():
            print(f"{name} is already open")
        else:
            check = self.check_pump(edge, True)
            if check[0]:
                edge.set_weight(True)
                for key in self.p_adj_dict:  # fix this lmao so it doesnt need to run a double for loop every time it opens a valve
                    for i in range(len(self.p_adj_dict[key])):
                        if self.p_adj_dict[key][i][1] == edge.get_name():
                            self.p_adj_dict[key][i][2] = True
            else:
                print(f"{name} cannot be opened: ")
            print(check[1])

    def close_valve(self, edge):
        name = edge.get_name()
        if isinstance(edge.get_src(), Chamber) and isinstance(edge.get_dest(), Chamber):
            if edge in self.arm_dict and self.arm_dict[edge].get_status():
                print(f"{name} cannot be closed, {self.arm_dict[edge].get_name()} is extended")
            else:
                if edge.get_weight():
                    edge.set_weight(False)
                    for key in self.c_adj_dict:  # fix this lmao
                        for i in range(len(self.c_adj_dict[key])):
                            if self.c_adj_dict[key][i][1] == edge.get_name():
                                self.c_adj_dict[key][i][2] = False
                    print(f"{name} is now closed")
        elif not edge.get_weight():
            print(f"{name} is already closed")
        else:
            check = self.check_pump(edge, False)
            if check[0]:
                edge.set_weight(False)
                for key in self.p_adj_dict:  # fix this lmao
                    for i in range(len(self.p_adj_dict[key])):
                        if self.p_adj_dict[key][i][1] == edge.get_name():
                            self.p_adj_dict[key][i][2] = False
            else:
                print(f"{name} cannot be closed: ")
            print(check[1])

    def extend_arm(self, arm):
        if arm.get_status():
            print(f"{arm.get_name()} is already extended")
        else:
            if arm.get_through_valve().get_weight():
                arm.set_status(True)
                print(f"{arm.get_name()} is now extended")
            else:
                print(f"cannot extend {arm.get_name()}, {arm.get_through_valve().get_name()} is closed")

    def retract_arm(self, arm):
        if not arm.get_status():
            print(f"{arm.get_name()} is already retracted")
        else:
            arm.set_status(False)
            print(f"{arm.get_name()} is now retracted")

    def fault_react(self, pump, op):
        if op:
            print(f"{pump.get_name()} has fault, closing nearby valves")
            for edge in self.fault_tracker[pump]:
                self.close_valve(edge)
        else:
            print(f"{pump.get_name()} fault is resolved, able to start running now")
