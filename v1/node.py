class Node:
    # initializes node instance
    def __init__(self, name, data):
        self.data = data # assigns data, Boolean type
        self.next = None # initializes next node as null (end)
        self.name = name # assigns name, String type

    def get_data(self):
        return self.data

    def set_data(self, new):
        self.data = new

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name
