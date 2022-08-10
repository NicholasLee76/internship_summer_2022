import time
from datetime import date
import queue
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from PyExpLabSys_master.PyExpLabSys.drivers.xgs600 import XGS600Driver

start = time.time()
x = []
backup_q = queue.Queue()
mmbe_q = queue.Queue()


def read_gauge(q, gauge):
    while True:
        lower_pressure = gauge.read_all_pressures()[2]
        q.put(lower_pressure)


def get_val(q):
    return q.get()


def plot_cont(func, param, xmax):
    y = []
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def update(i):
        yi = func(param)
        y.append(yi)
        x.append(int(time.time()-start))
        ax.clear()
        ax.plot(x, y)
        ax.set_xlabel('elapsed time (s)')
        ax.set_ylabel('pressure (torr)')
        ax.set_title(f'backup chamber pressure ({date.today()})')
        print(f"{i}: {yi} @ {x[-1]} seconds")
        time.sleep(0.5)

    a = anim.FuncAnimation(fig, update, frames=xmax, repeat=False)
    plt.show()


def main(s):
    g1 = XGS600Driver(port='/dev/cu.usbserial-110') #replace with appropriate comm port for windows

    threading.Thread(target=read_gauge, args=(backup_q, g1, ), daemon=True).start()

    plot_cont(get_val, backup_q, s)


if __name__ == '__main__':
    main(1000)
