from PyExpLabSys_master.PyExpLabSys.drivers.pfeiffer_turbo_pump import TurboDriver


def main():
    t = TurboDriver(adress=1, port='/dev/cu.usbserial-A107ZQKT')  # check to make sure usb port parameter is correct
    print(t.read_rotation_speed())
    #t.turn_pump_on()
    #print(t.read_rotation_speed())


if __name__ == '__main__':
    main()
