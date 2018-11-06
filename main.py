import numpy as np
import math
import matplotlib.pyplot as plt

NUM_PTS = 1000


def generate_anomaly_unsmooth():

    def generate_splash():
        if np.random.randn() > 2.1:
            x = np.random.uniform(-50, 50)
        else:
            x = 0
        return x

    a_date = np.linspace(0, NUM_PTS, NUM_PTS+1)
    anomaly = []
    for i in a_date:
        anomaly.append((
            i,
            generate_splash(),
            generate_splash(),
            generate_splash(),
            generate_splash(),
            generate_splash(),
            generate_splash(),
            generate_splash(),
            generate_splash()
       ))
    return anomaly


def generate_data(n=NUM_PTS):
    a_date = np.linspace(0, n, n+1)
    a_gases = []
    a_ano = generate_anomaly_unsmooth()
    for i in a_date:
        a_gases.append((
            i,
            50 + i / 100 + 7 * math.sin(i / 25) + 6 * math.sin(i / 10) + 5 * math.sin(i / 5) + np.random.randn(),
            30 + i / 50 + 4 * math.sin(i / 15) + 10 * math.sin(i / 25) + 9 * math.sin(i / 35) + np.random.randn(),
            70 + i / 80 + 5 * math.sin(i / 30) + 4 * np.random.randn(),
            20 + i / 30 + 3 * math.log(4 * i + 1) + 11 * math.sin(i / 40) + 8 * math.sin(i / 34)
                + 2 * math.sin(i / 10) + 3 * math.sin(i / 5)
                + np.random.randn(),
            #generating CH4
			60 + i / 80 + 3 * math.sin(i / 15) + 5 * math.sin(i / 70) + np.random.randn(),
            #generating C2H2
			20 + i / 80 + 4 * math.sin(i / 50) + np.random.randn(),
            #generating C2H6
            20 + i / 20 + 5 * math.sin(i / 4) + 15 * math.sin(i / 35) + 12 * math.sin(i / 68) + 4 * np.random.randn(),
            #generating O2
            50 + i / 100 + 10 * math.sin(i / 10) + 5 * math.sin(i / 4) + 2 * np.random.randn()
        ))
    return np.array(a_gases) + np.array(a_ano)


def show_graph():
    gases = generate_data()
    fig, ((ax_h2, ax_co), (ax_co2, ax_ch4), (ax_c2h2, ax_c2h4), (ax_c2h6, ax_o2)) = plt.subplots(4, 2, sharex='all')

    ax_h2.set_ylim(0, 100)
    ax_h2.set_title('H2')
    ax_h2.plot((gases[:,0]), gases[:,1], color='red')

    ax_co.set_ylim(0, 100)
    ax_co.set_title('CO')
    ax_co.plot((gases[:, 0]), gases[:, 2])

    ax_co2.set_ylim(0, 100)
    ax_co2.set_title('CO2')
    ax_co2.plot((gases[:, 0]), gases[:, 3])

    ax_ch4.set_ylim(0, 100)
    ax_ch4.set_title('CH4')
    ax_ch4.plot((gases[:, 0]), gases[:, 4])

    ax_c2h2.set_ylim(0, 100)
    ax_c2h2.set_title('C2H2')
    ax_c2h2.plot((gases[:, 0]), gases[:, 5])

    ax_c2h4.set_ylim(0, 100)
    ax_c2h4.set_title('C2H4')
    ax_c2h4.plot((gases[:, 0]), gases[:, 6])

    ax_c2h6.set_ylim(0, 100)
    ax_c2h6.set_title('C2H6')
    ax_c2h6.plot((gases[:, 0]), gases[:, 7])

    ax_o2.set_ylim(0, 100)
    ax_o2.set_title('O2')
    ax_o2.plot((gases[:, 0]), gases[:, 8], color='green')
    plt.show()


def show_graph1():
    gases = generate_data(NUM_PTS)
    np.savetxt('a.csv', gases, delimiter=';', fmt='%.3f')
    fig, ax = plt.subplots()
    ax.plot((gases[:,0]), gases[:,1], label='H2')
    ax.plot((gases[:, 0]), gases[:, 2], label='CO')
    ax.plot((gases[:, 0]), gases[:, 3], label='CO2')
    ax.plot((gases[:, 0]), gases[:, 4], label='CH4')
    ax.plot((gases[:, 0]), gases[:, 5], label='C2H2')
    ax.plot((gases[:, 0]), gases[:, 6], label='C2H4')
    ax.plot((gases[:, 0]), gases[:, 7], label='C2H6')
    plt.legend()
    plt.show()


show_graph()
#generate_data()