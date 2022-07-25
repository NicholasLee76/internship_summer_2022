class Arm:
    def __init__(self, name, through_valve, status):
        self.name = name  # assigns name, String type
        self.valve = through_valve # assigns which valves arm goes through, Edge type (may make this a list for more general use)
        self.status = False  # assigns whether arm is retracted or extended, Boolean type (T: extended, F: retracted)

    def get_name(self):
        return self.name

    def get_through_valve(self):
        return self.valve

    def get_status(self):
        return self.status

    def set_status(self, new):
        self.status = new

