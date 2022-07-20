import math


class Node:
    # initializes node instance
    def __init__(self, name, data):
        self.data = data # assigns data, String type
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


class Chamber(Node):
    def __init__(self, name, pressure):
        self.pressure = pressure  # assigns chamber pressure (torr), Double type
        data = ""
        if pressure >= 750:
            data = "atmosphere"
        elif math.log10(pressure) > -4:
            data = "mid"
        elif math.log10(pressure) > -9:
            data = "vacuum"
        elif math.log10(pressure) >= -11:
            data = "ultra high vacuum"
        Node.__init__(self, name, data)

    def get_pressure(self):
        return self.pressure

    def set_pressure(self, new):
        self.pressure = new
        self.update_data()

    def update_data(self):
        if self.pressure >= 750:
            super().set_data("atmosphere")
        elif math.log10(self.pressure) >= -4:
            super().set_data("mid")
        elif math.log10(self.pressure) >= -9:
            super().set_data("vacuum")
        elif math.log10(self.pressure) >= -12:
            super().set_data("ultra high vacuum")


class Pump(Node):
    def __init__(self, name, run_status):
        self.name = name  # assigns name, String type
        self.run_status = run_status  # assigns whether pump is running, Boolean type (T: running, F: stopping)

    def get_name(self):
        return self.name

    def get_status(self):
        return self.run_status

    def set_status(self, new):
        self.run_status = new

    def __str__(self):
        return self.name


class Turbo(Pump):
    def __init__(self, name, speed):
        self.speed = speed  # assigns fan speed (rps), Int type
        if self.speed <= 1000: # this value may change based on what the high and low setting speeds are
            run_status = False
        else:
            run_status = True
        Pump.__init__(self, name, run_status)

    def get_speed(self):
        return self.speed


class Cryo(Pump):
    def __init__(self, name, temp):
        self.temp = temp  # assigns cryo temp (K), Int type
        if self.temp >= 60:  # i should figure out what value this is lmao
            run_status = False
        else:
            run_status = True
        Pump.__init__(self, name, run_status)

    def get_temp(self):
        return self.temp
