import web
import pickle
import matplotlib.pyplot as plt
import numpy as np
import sys

def line_weekly_change_only():

    chains = pickle.load(open('q4_stats_weekly.p', 'rb'))

    x_axis = [i for i in range(1, 10)]

    legend = []

    for chain in chains:

        if chain == 'costco':
            continue

        location_count = 0
        y_axis = np.zeros(9)

        for stat in chains[chain]:

            if None in stat:
                continue

            if stat[0] == stat[8]:
                continue

            y_axis += np.asarray(stat)
            location_count += 1

        y_axis -= y_axis.item(0)
        # y_axis /= location_count

        legend.append(chain)
        plt.plot(x_axis, y_axis)

    plt.legend(legend, loc='upper left')
    plt.xlabel('Week')
    plt.ylabel('Total visits since Week 1')
    plt.show()

def line_weekly():

    chains = pickle.load(open('q4_stats_weekly.p', 'rb'))

    x_axis = [i for i in range(1, 10)]

    legend = []

    for chain in chains:

        if chain == 'costco':
            continue

        location_count = 0
        y_axis = np.zeros(9)

        for stat in chains[chain]:

            # TODO: Figure out better method to use None

            if None in stat or 0 in stat:
                continue

            y_axis += np.asarray(stat)
            location_count += 1

        y_axis -= y_axis.item(0)
        # y_axis /= location_count

        legend.append(chain)
        plt.plot(x_axis, y_axis)

    plt.legend(legend, loc='upper left')
    plt.xlabel('Week')
    plt.ylabel('Total visits since Week 1')
    plt.show()




    # print chains['starbucks']


line_weekly_change_only()
