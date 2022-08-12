import time
from datetime import date
import queue
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from PyExpLabSys_master.PyExpLabSys.drivers.xgs600 import XGS600Driver

start = time.time()
x = []
mmbe_q = queue.Queue()


def read_gauge(q, gauge, num):
    while True:
        pressure = gauge.read_all_pressures()[num]
        q.put(pressure)


def get_val(q):
    return q.get()


def plot_cont(func, param, xmax):
    y = []
    fig, ax = plt.subplots()

    def update(i):
        yi = func(param)
        y.append(yi)
        x.append(int(time.time()-start))
        ax.clear()
        ax.annotate(f'pressure: {y[-1]}', xycoords='figure fraction', xy=(0.15, 0.8))
        plt.yscale('log')
        plt.ylim(1 * 10**-9, 1.5*max(y))
        ax.plot(x, y)
        ax.set_xlabel('elapsed time (s)')
        ax.set_ylabel('pressure (torr)')
        ax.set_title(f'mmbe chamber pressure ({date.today()})')
        print(f"{i}: {yi} @ {x[-1]} seconds")
        time.sleep(0.1)

    a = anim.FuncAnimation(fig, update, frames=xmax, repeat=False)
    plt.show()


def main(s):
    g1 = XGS600Driver(port='/dev/cu.usbserial-210') #replace with appropriate comm port for windows

    threading.Thread(target=read_gauge, args=(mmbe_q, g1, 2), daemon=True).start()

    plot_cont(get_val, mmbe_q, s)


if __name__ == '__main__':
    main(1000)
