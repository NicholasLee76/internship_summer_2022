from data import chambers, pumps, valves
from vacuum_system import VacuumSystem
from tkinter import *

master = Tk()

TYPE = StringVar(master)
INSTRUMENT = StringVar(master)
OPERATION = StringVar(master)
VALUE = StringVar(master)

COMMAND = [None] * 3

uhv = VacuumSystem(chambers, pumps, valves)


def new_command():
    pick_type = OptionMenu(master, TYPE, *['chamber', 'pump', 'valve', 'arm'])
    pick_type.pack()

    b1 = Button(master, text="SELECT TYPE", command=select_type)
    b1.pack()


def select_type():
    if TYPE.get() == 'pump':
        pick_ins = OptionMenu(master, INSTRUMENT, *[ins.get_name() for ins in pumps])
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
        pass # arm stuff


def select_ins():
    COMMAND[0] = INSTRUMENT.get()
    if TYPE.get() == 'pump':
        pick_op = OptionMenu(master, OPERATION, *['run', 'stop running']) # add a break/fault option
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'chamber':
        pick_op = OptionMenu(master, OPERATION, *['change pressure'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'valve':
        pick_op = OptionMenu(master, OPERATION, *['open', 'close'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    else:
        pass # arm stuff


def select_op():
    COMMAND[1] = OPERATION.get()
    if TYPE.get() == 'chamber':
        pick_val = OptionMenu(master, VALUE, *['760', 10**-7, 10**-11])
        pick_val.pack()
        b4 = Button(master, text="SELECT PRESSURE", command=select_val)
        b4.pack()
    select_val()


def select_val():
    COMMAND[2] = VALUE.get()
    print(COMMAND)
    execute_command()


def execute_command():
    ins = None
    if TYPE.get() == 'chamber':
        for obj in chambers:
            if obj.get_name() == COMMAND[0]:
                ins = obj

        ins.set_pressure(float(COMMAND[2]))
    elif TYPE.get() == 'valve':
        for obj in valves:
            if obj.get_name() == COMMAND[0]:
                ins = obj
        if COMMAND[1] == 'open':
            uhv.open_valve(ins)
        else:
            uhv.close_valve(ins)
    elif TYPE.get() == 'pump':
        for obj in pumps:
            if obj.get_name() == COMMAND[0]:
                ins = obj
        if COMMAND[1] == 'run':
            ins.set_status(True)
        else:
            ins.set_status(False)
    else:
        pass # arm stuff
    print(uhv)

    for widget in master.winfo_children():
        widget.pack_forget()
    b1 = Button(master, text="NEW COMMAND", command=new_command)
    b1.pack()


def main():
    print(uhv)

    new_command()

    mainloop()


if __name__ == '__main__':
    main()
