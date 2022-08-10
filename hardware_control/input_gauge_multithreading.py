import threading
import math
import queue
from PyExpLabSys_master.PyExpLabSys.drivers.xgs600 import XGS600Driver


lower_q = queue.Queue()
mmbe_q = queue.Queue()
command_q = queue.Queue()

user_input = ''


def exec_user_input():
    global user_input
    user_input = ''


def execute_command(q):
    command = q.get()
    print(command)  # add some other function for executing commands later
    command_q.put(command)


def gauge_input(q):
    while True:
        if math.log10(q.get()) >= -7:
            print(q.get())
            print('not ultra high vacuum')
            command_q.put('chamber pressure bad')
        elif math.log10(q.get()) <= 13:
            print(q.get())
            print('ultra high vacuum')
        q.task_done()


def get_input():
    global user_input
    user_input = input('command: ')


def main():
    g1 = XGS600Driver(port='/dev/cu.usbserial-110')

    threading.Thread(target=get_input, daemon=True).start()
    threading.Thread(target=gauge_input, args=(lower_q, ), daemon=True).start()
    threading.Thread(target=gauge_input, args=(mmbe_q, ), daemon=True).start()

    while True:
        if user_input != '':
            print(f"command: {user_input}")
            exec_user_input()

        else:
            lower = g1.read_all_pressures()[5]
            mmbe = g1.read_all_pressures()[2]
            lower_q.put(lower)
            mmbe_q.put(mmbe)


if __name__ == '__main__':
    main()


