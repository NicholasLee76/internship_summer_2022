from data import chambers, pumps, valves, arms
from vacuum_system_v3 import VacuumSystem
from tkinter import *
import cv2
import pickle

master = Tk()

PROCESS = StringVar(master)

COMMAND = [None] * 3
with open('operations.pckl', 'rb') as file:
    OPERATIONS = pickle.load(file)

uhv = VacuumSystem(chambers, pumps, valves, arms)


def select_op():
    master.destroy()


def execute_operation(command):
    ins = None
    for obj in chambers + valves + pumps + arms:
        if obj.get_name() == command[1]:
            ins = obj

    if command[0] == 'chamber':
        if command[2] == 'pump down':
            uhv.pump_down(ins)
        elif command[2] == 'vent':
            uhv.vent(ins)
        else:
            ins.set_pressure(760)
            uhv.chamber_react(ins)

    elif command[0] == 'valve':
        if command[2] == 'open':
            uhv.open_valve(ins)
        else:
            uhv.close_valve(ins)

    elif command[0] == 'turbo':
        fix = False
        if command[2] == 'run at high speed':
            ins.set_speed(1500)
            print(f"{ins} is running at high speed")
        elif command[2] == 'run at low speed':
            ins.set_speed(1350)
            print(f"{ins} is running at low speed")
        elif command[2] == 'stop running':
            ins.set_speed(0)
            print(f"{ins} is not running")
        elif command[2] == 'break':
            ins.set_fault(True)
        elif command[2] == 'fix':
            ins.set_fault(False)
            fix = True
        uhv.status_react(ins, fix)

    elif command[0] == 'cryo':
        fix = False
        if command[2] == 'cool down (run)':
            ins.set_temp(50)
        elif command[2] == 'heat up (stop)':
            ins.set_temp(70)
        elif command[2] == 'break':
            ins.set_fault(True)
        elif command[2] == 'fix':
            ins.set_fault(False)
            fix = True
        uhv.status_react(ins, fix)

    elif command[0] == 'arm':
        if command[2] == 'extend':
            uhv.extend_arm(ins)
        else:
            uhv.retract_arm(ins)

    print(uhv)


def main():
    print(uhv)

    img = cv2.imread("diagram.png", 1)
    cv2.imshow('diagram', img)

    pick_op = OptionMenu(master, PROCESS, *[key for key in OPERATIONS])
    pick_op.pack()
    b1 = Button(master, text="SELECT TYPE", command=select_op)
    b1.pack()

    mainloop()

    key = PROCESS.get()
    for command in OPERATIONS[key]:
        execute_operation(command)


if __name__ == '__main__':
    main()
