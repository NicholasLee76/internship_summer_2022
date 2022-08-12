from relay_ft245r.relay_ft245r import FT245R
from usb.backend import libusb1

be = libusb1.get_backend(find_library=lambda x: "python3-libusb1")
VENDOR_ID = 0x0403
PRODUCT_ID = 0x6001
user_input = ''


def get_user_input():
    global user_input
    user_input = input('type relay_num and on or off: ')


def reset_input():
    global user_input
    user_input = ''


def main(relays):
    rb = FT245R()
    dev_list = rb.list_dev(be)
    rb.connect(dev_list[0])

    for relay in relays:
        rb.switchon(relay)

    get_user_input()
    while True:
        if user_input != '':
            print(f'turning {user_input.split()[1]} {user_input.split()[0]}')
            if user_input.split()[1] == 'off':
                rb.switchoff(int(user_input.split()[0]))
            elif user_input.split()[1] == 'on':
                rb.switchon(int(user_input.split()[0]))
            else:
                print('invalid command: use form [relay_num] [command (on or off)]')
            reset_input()
            get_user_input()


if __name__ == '__main__':
    main([])

