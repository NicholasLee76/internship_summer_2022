from data import chambers, pumps, valves, arms
from vacuum_system_v2 import VacuumSystem
from node import Turbo, Cryo
from tkinter import *

master = Tk()

TYPE = StringVar(master)
INSTRUMENT = StringVar(master)
OPERATION = StringVar(master)
VALUE = StringVar(master)

COMMAND = [None] * 3

uhv = VacuumSystem(chambers, pumps, valves, arms)


def new_command():
    pick_type = OptionMenu(master, TYPE, *['chamber', 'turbo', 'cryo', 'valve', 'arm'])
    pick_type.pack()

    b1 = Button(master, text="SELECT TYPE", command=select_type)
    b1.pack()


def select_type():
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
    COMMAND[0] = INSTRUMENT.get()
    if TYPE.get() == 'turbo':
        pick_op = OptionMenu(master, OPERATION, *['run at high speed', 'run at low speed', 'stop running', 'vent', 'break', 'fix'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'cryo':
        pick_op = OptionMenu(master, OPERATION, *['cool down (run)', 'heat up (stop)', 'vent', 'break', 'fix'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'chamber':
        pick_op = OptionMenu(master, OPERATION, *['change pressure', 'vent'])
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
    COMMAND[1] = OPERATION.get()
    if TYPE.get() == 'chamber' and OPERATION.get() == 'change pressure':
        pick_val = OptionMenu(master, VALUE, *['760.0', 10 ** -7, 10 ** -11])
        pick_val.pack()
        b4 = Button(master, text="SELECT PRESSURE", command=select_val)
        b4.pack()
    else:
        select_val()


def select_val():
    COMMAND[2] = VALUE.get()
    execute_command()


def execute_command():
    ins = None
    for obj in chambers + valves + pumps + arms:
        if obj.get_name() == COMMAND[0]:
            ins = obj

    if TYPE.get() == 'chamber':
        if COMMAND[1] == 'change pressure':
            ins.set_pressure(float(COMMAND[2]))
        elif COMMAND[1] == 'vent':
            uhv.vent(ins)

    elif TYPE.get() == 'valve':
        if COMMAND[1] == 'open':
            uhv.open_valve(ins)
        else:
            uhv.close_valve(ins)

    elif TYPE.get() == 'turbo':
        fix = False
        if COMMAND[1] == 'run at high speed':
            ins.set_speed(1500)
            print(f"{ins} is running at high speed")
        elif COMMAND[1] == 'run at low speed':
            ins.set_speed(1350)
            print(f"{ins} is running at low speed")
        elif COMMAND[1] == 'stop running':
            ins.set_speed(0)
            print(f"{ins} is not running")
        elif COMMAND[1] == 'break':
            ins.set_fault(True)
        elif COMMAND[1] == 'fix':
            ins.set_fault(False)
            fix = True
        if COMMAND[1] != 'vent':
            uhv.status_react(ins, fix)
        else:
            pass # uhv.vent(ins) vent stuff

    elif TYPE.get() == 'cryo':
        fix = False
        if COMMAND[1] == 'cool down (run)':
            ins.set_temp(50)
        elif COMMAND[1] == 'heat up (stop)':
            ins.set_temp(70)
        elif COMMAND[1] == 'break':
            ins.set_fault(True)
        elif COMMAND[1] == 'fix':
            ins.set_fault(Ffrom data import chambers, pumps, valves, arms
from vacuum_system_v2 import VacuumSystem
from node import Turbo, Cryo
from tkinter import *

master = Tk()

TYPE = StringVar(master)
INSTRUMENT = StringVar(master)
OPERATION = StringVar(master)
VALUE = StringVar(master)

COMMAND = [None] * 3

uhv = VacuumSystem(chambers, pumps, valves, arms)


def new_command():
    pick_type = OptionMenu(master, TYPE, *['chamber', 'turbo', 'cryo', 'valve', 'arm'])
    pick_type.pack()

    b1 = Button(master, text="SELECT TYPE", command=select_type)
    b1.pack()


def select_type():
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
    COMMAND[0] = INSTRUMENT.get()
    if TYPE.get() == 'turbo':
        pick_op = OptionMenu(master, OPERATION, *['run at high speed', 'run at low speed', 'stop running', 'vent', 'break', 'fix'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'cryo':
        pick_op = OptionMenu(master, OPERATION, *['cool down (run)', 'heat up (stop)', 'vent', 'break', 'fix'])
        pick_op.pack()
        b3 = Button(master, text="SELECT OPERATION", command=select_op)
        b3.pack()
    elif TYPE.get() == 'chamber':
        pick_op = OptionMenu(master, OPERATION, *['change pressure', 'vent'])
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
    COMMAND[1] = OPERATION.get()
    if TYPE.get() == 'chamber' and OPERATION.get() == 'change pressure':
        pick_val = OptionMenu(master, VALUE, *['760.0', 10 ** -7, 10 ** -11])
        pick_val.pack()
        b4 = Button(master, text="SELECT PRESSURE", command=select_val)
        b4.pack()
    else:
        select_val()


def select_val():
    COMMAND[2] = VALUE.get()
    execute_command()


def execute_command():
    ins = None
    for obj in chambers + valves + pumps + arms:
        if obj.get_name() == COMMAND[0]:
            ins = obj

    if TYPE.get() == 'chamber':
        if COMMAND[1] == 'change pressure':
            ins.set_pressure(float(COMMAND[2]))
        elif COMMAND[1] == 'vent':
            uhv.vent(ins)

    elif TYPE.get() == 'valve':
        if COMMAND[1] == 'open':
            uhv.open_valve(ins)
        else:
            uhv.close_valve(ins)

    elif TYPE.get() == 'turbo':
        fix = False
        if COMMAND[1] == 'run at high speed':
            ins.set_speed(1500)
            print(f"{ins} is running at high speed")
        elif COMMAND[1] == 'run at low speed':
            ins.set_speed(1350)
            print(f"{ins} is running at low speed")
        elif COMMAND[1] == 'stop running':
            ins.set_speed(0)
            print(f"{ins} is not running")
        elif COMMAND[1] == 'break':
            ins.set_fault(True)
        elif COMMAND[1] == 'fix':
            ins.set_fault(False)
            fix = True
        if COMMAND[1] != 'vent':
            uhv.status_react(ins, fix)
        else:
            pass # uhv.vent(ins) vent stuff

    elif TYPE.get() == 'cryo':
        fix = False
        if COMMAND[1] == 'cool down (run)':
            ins.set_temp(50)
        elif COMMAND[1] == 'heat up (stop)':
            ins.set_temp(70)
        elif COMMAND[1] == 'break':
            ins.set_fault(True)
        elif COMMAND[1] == 'fix':
            ins.set_fault(False)
            fix = True
        if COMMAND[1] != 'vent':
            uhv.status_react(ins, fix)
        else:
            # uhv.vent(ins)
            pass # vent stuff

    elif TYPE.get() == 'arm':
        if COMMAND[1] == 'extend':
            uhv.extend_arm(ins)
        else:
            uhv.retract_arm(ins)

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
alse)
            fix = True
        if COMMAND[1] != 'vent':
            uhv.status_react(ins, fix)
        else:
            # uhv.vent(ins)
            pass # vent stuff

    elif TYPE.get() == 'arm':
        if COMMAND[1] == 'extend':
            uhv.extend_arm(ins)
        else:
            uhv.retract_arm(ins)

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
