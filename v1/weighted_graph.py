from node import Node
from edge import Edge


class Weighted_Graph:
    def __init__(self, vertices, edges):
        self.adj_dict = {}
        for vertex in vertices:
            self.adj_dict.update({vertex : []})

        for edge in edges:
            prev = self.adj_dict[edge.get_src()]
            temp = [edge.get_dest(), edge.get_name(), edge.get_weight()]
            prev.append(temp)
            self.adj_dict.update({edge.get_src() : prev})

            prev = self.adj_dict[edge.get_dest()]
            temp = [edge.get_src(), edge.get_name(), edge.get_weight()]
            prev.append(temp)
            self.adj_dict.update({edge.get_dest() : prev})


    def __str__(self):
        # prints adjacency lists for each node, including connecting edge
        ret = ""
        for key in self.adj_dict.keys():
            ret += (key.get_name() + ": ")
            '''for node in self.adj_dict[key]:
                name = node[0]
                adj_edge = node[1]
                edge_weight = node[2]'''
            for i in range(len(self.adj_dict[key])):
                name = self.adj_dict[key][i][0]
                adj_edge = self.adj_dict[key][i][1]
                edge_weight = self.adj_dict[key][i][2]
                ret += (f"({name}, {adj_edge}, {edge_weight}) ")
                '''if adj_edge == "gv4":
                    print(id(self.adj_dict[key][i]))'''
            ret += "\n"
        return ret


    def check_subgraph(self, edge):
        # gets list of adjacent subgraph edges excluding given edge
        n1 = edge.get_src()
        n2 = edge.get_dest()
        adj_list1 = self.adj_dict[n1].copy()
        adj_list2 = self.adj_dict[n2].copy()
        for i in range(len(adj_list1)):
            if adj_list1[i][0] == n2:
                adj_list1.pop(i)
                break
        for i in range(len(adj_list2)):
            if adj_list2[i][0] == n1:
                adj_list2.pop(i)
                break
        edge_list = adj_list1 + adj_list2
        # checks edges and src dest nodes
        sum = 0
        bad_edges = []
        bad_nodes = []

        for i in range(len(edge_list)):
            if edge_list[i][2]:
                sum += 1
                bad_edges.append(edge_list[i][1])
        if edge.get_src().get_data() == False:
            sum += 1
            bad_nodes.append(edge.get_src().get_name())
        if edge.get_dest().get_data() == False:
            sum += 1
            bad_nodes.append(edge.get_dest().get_name())

        if sum == 0 and edge.get_weight() == False:
            return [True, f"{edge} can be opened"]
        elif sum == 0 and edge.get_weight():
            return [True, f"{edge} is already open"]
        else:
            return [False, bad_edges, bad_nodes]


    def open_valve(self, edge):
        name = edge.get_name()
        check = self.check_subgraph(edge)
        if check[0]:
            edge.set_weight(True)
            for key in self.adj_dict.keys():
                for i in range(len(self.adj_dict[key])):
                    if self.adj_dict[key][i][1] == edge.get_name():
                         self.adj_dict[key][i][2] = True
            print(f"{name} is now open")

        else:
            print(f"{name} cannot be opened:")
            for bad_edge in check[1]:
                print(f"{bad_edge} is open\n")
            for bad_node in check[2]:
                print(f"{bad_node} has incorrect pressure\n")


    def close_valve(self, edge):
        name = edge.get_name()
        if edge.get_weight():
            edge.set_weight(False)
            for key in self.adj_dict.keys():
                for i in range(len(self.adj_dict[key])):
                    if self.adj_dict[key][i][1] == edge.get_name():
                         self.adj_dict[key][i][2] = False
            print(f"{name} is now closed")
        else:
            print(f"{name} is already closed")
