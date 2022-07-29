from data import chambers, pumps, valves, arms
from vacuum_system_v3 import VacuumSystem
from node import Turbo, Cryo
from tkinter import *
import pickle
import cv2

master = Tk()

START = StringVar(master)
TYPE = StringVar(master)
INSTRUMENT = StringVar(master)
OPERATION = StringVar(master)
VALUE = StringVar(master)
PROCESS = StringVar(master)

COMMAND = [None] * 3

with open('operations.pckl', 'rb') as file:
    OPERATIONS = pickle.load(file)

uhv = VacuumSystem(chambers, pumps, valves, arms)


def start():
    start_pick = OptionMenu(master, START, *['add process', 'update process'])
    start_pick.pack()

    b = Button(master, text="START", command=add_or_update)
    b.pack()


def add_or_update():
    if START.get() == 'add process':
        add_process()
    elif START.get() == 'update process':
        pick_process()


def add_process():
    proc = input("new process: ")
    OPERATIONS.update({proc: []})
    pick_process()


def pick_process():
    pick = OptionMenu(master, PROCESS, *OPERATIONS)
    pick.pack()

    b = Button(master, text="SELECT PROCESS", command=new_command)
    b.pack()


def new_command():
    pick_type = OptionMenu(master, TYPE, *['chamber', 'turbo', 'cryo', 'valve', 'arm'])
    pick_type.pack()

    b1 = Button(master, text="SELECT TYPE", command=select_type)
    b1.pack()


def select_type():
    COMMAND[0] = TYPE.get()
    if TYPE.get() == 'turbo':
        pick_ins = OptionMenu(master, INSTRUMENT, *[ins.get_name() for ins in pumps if isinstance(ins, Turbo)])
        pick_ins.pack()
        b2 = Button(master, text="SELECT PUMP", command=select_ins)
        b2.pack()
    elif TYPE.get() == 'cryo':
        pick_ins = OptionMenu(master, INSTRUMENT, *[ins.get_name() for ins in pumps if isinstance(ins, Cryo)])
        pick_ins.pack()
        b2 = Button(master, text="SELECT PUMP", command=select_ins)
        b2.pack()
    elif TYPE.get() == 'chamber':
        pick_ins = OptionMenu(master, INSTRUMENT, *[ins.get_name() for ins in chambers])
        pick_ins.pack()
        b2 = Button(master, text="SELECT CHAMBER", command=select_ins)
        b2.pack()
    elif TYPE.get() == 'valve':
        pick_ins = OptionMenu(master, INSTRUMENT, *[ins.get_name() for ins in valves])
        pick_ins.pack()
        b2 = Button(master, text="SELECT VALVE", command=select_ins)
        b2.pack()
    else:
        pick_ins = OptionMenu(master, INSTRUMENT, *[ins.get_name() for ins in arms])
        pick_ins.pack()
        b2 = Button(master, text="SELECT ARM", command=select_ins)
        b2.pack()


def select_ins():
    COMMAND[1] = INSTRUMENT.get()
    if TYPE.get() == 'turbo':
        pick_op = OptionMenu(master, OPERATION, *['run at high speed', 'run at low speed', 'stop running', 'break', 'fix'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'cryo':
        pick_op = OptionMenu(master, OPERATION, *['cool down (run)', 'heat up (stop)', 'break', 'fix'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'chamber':
        pick_op = OptionMenu(master, OPERATION, *['pump down', 'vent', 'break'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'valve':
        pick_op = OptionMenu(master, OPERATION, *['open', 'close'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    else:
        pick_op = OptionMenu(master, OPERATION, *['extend', 'retract'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()


def select_op():
    COMMAND[2] = OPERATION.get()
    if TYPE.get() == 'chamber' and OPERATION.get() == 'change pressure':
        pick_val = OptionMenu(master, VALUE, *['760.0', 10 ** -7, 10 ** -11])
        pick_val.pack()
        b4 = Button(master, text="SELECT PRESSURE", command=select_val)
        b4.pack()
    else:
        select_val()


def select_val():
    prev = OPERATIONS[PROCESS.get()]
    prev.append(COMMAND.copy())
    OPERATIONS.update({PROCESS.get(): prev})
    print(f"{COMMAND[2]} {COMMAND[1]}")
    for widget in master.winfo_children():
        widget.pack_forget()
    q = input("keep recording? y or n: ")
    if q == 'y' or q == 'Y':
        b1 = Button(master, text="NEW COMMAND", command=new_command)
        b1.pack()
    else:
        master.destroy()


def main():
    img = cv2.imread("diagram.png", 1)
    cv2.imshow('diagram', img)
    start()
    mainloop()
    print(OPERATIONS[PROCESS.get()])
    f = open('operations.pckl', 'wb')
    pickle.dump(OPERATIONS, f)
    f.close()
    with open('operations.pckl', 'rb') as f:
        ops = pickle.load(f)


if __name__ == '__main__':
    main()


