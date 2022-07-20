class Edge:
    # initializes edge instance
    def __init__(self, src, dest, name, weight):
        self.src = src # starting point, Node type
        self.dest = dest # ending point, Node type
        self.name = name # name, String type
        self.weight = weight # weight, Boolean type

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def set_weight(self, new):
        self.weight = new
