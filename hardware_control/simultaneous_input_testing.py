import threading
import math
import queue
import time
import random
from PyExpLabSys_master.PyExpLabSys.drivers.xgs600 import XGS600Driver

command_q = queue.Queue()
user_input = ''


def exec_command():
    command = command_q.get()
    print(f'executing: {command}')


def get_user_input():
    global user_input
    user_input = input('command: ')


def reset_user_input():
    global user_input
    user_input = ''


def main():
    #g = XGS600Driver(port='/dev/cu.usbserial-210')
    threading.Thread(target=get_user_input).start()

    while True:
        if user_input != '':
            command_q.put(user_input)
            reset_user_input()
            exec_command()
            get_user_input()
        else:
            #backup = g.read_all_pressures()[5]
            backup = random.random()
            if backup > 1:
                command_q.put(backup)
                exec_command()


if __name__ == '__main__':
    main()
