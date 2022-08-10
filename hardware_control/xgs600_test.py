import math
from PyExpLabSys_master.PyExpLabSys.drivers.xgs600 import XGS600Driver


def main():
    g = XGS600Driver(port='/dev/cu.usbserial-110')  # check to make sure usb port parameter is correct
    print(g.list_all_gauges())
    while True:
        print(f"lower chamber: {g.read_all_pressures()[5]:1E}, mmbe chamber: {g.read_all_pressures()[2]:1E}")


if __name__ == '__main__':
    print("a")
    main()
