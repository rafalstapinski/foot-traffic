import web
import pickle
from tabulate import tabulate
import numpy as np
from scipy import stats as sp_stats

def rate_of_increase(change_only = False):

    chains = pickle.load(open('q4_stats_weekly.p', 'rb'))

    x = [i for i in range(1, 10)]

    table = [[
        'chain', 'unweighted rate', 'weighted rate'
    ]]

    for chain in chains:

        if chain == 'costco':
            continue

        y = np.zeros(9)
        location_count = 0

        for stat in chains[chain]:

            if None in stat or 0 in stat:
                continue

            start = next(i for i in stat if i != None)
            end = next(i for i in reversed(stat) if i != None)

            if change_only and start == end:
                continue

            y += np.asarray(stat)
            location_count += 1

        unw_slope, intercept, r_value, p_value, std_err = sp_stats.linregress(x, y)

        y /= location_count

        w_slope, intercept, r_value, p_value, std_err = sp_stats.linregress(x, y)

        table.append([chain, unw_slope, w_slope])

    print tabulate(table)

def to_csv():

    chains = pickle.load(open('stats.p', 'rb'))

    stats_file_str = 'chain,start,end,change,percent change\n'

    for chain in chains:
        for stat in chains[chain]:
            if stat[0] != 0:

                change = stat[1] - stat[0]
                percent_change = float(change) / float(stat[0])

                stats_file_str += '%s,%d,%d,%d,%f\n' % (
                    chain,
                    stat[0],
                    stat[1],
                    change,
                    percent_change
                )

    stats_file = open('stats.csv', 'w')
    stats_file.write(stats_file_str)
    stats_file.close()


def summary(change_only = False):

    stats = pickle.load(open('q4_stats_weekly.p', 'rb'))

    table = [[
        'chain name', 'location count', 'total checkins at start',
        'total checkins at end', 'avg location change', 'avg location % change'
    ]]

    for chain in stats:

        if chain == 'costco':
            continue

        locations_count = 0
        total_start = 0
        total_end = 0
        avg_change = 0
        avg_percent_change = 0

        for stat in stats[chain]:

            k = 0

            for z in stat:
                if z == None:
                    k += 1

            if k > 2:
                continue # closed down starbucks

            start = next(i for i in stat if i != None)
            end = next(i for i in reversed(stat) if i != None)

            if start == 0 or end == 0:
                continue

            if change_only and end == start:
                continue

            locations_count += 1

            total_start += start
            total_end += end

            change = end - start
            percent_change = float(change) / float(start)

            avg_change += change
            avg_percent_change += percent_change

        avg_change /= float(locations_count)
        avg_percent_change /= float(locations_count) / 100

        table.append([
            chain, locations_count, total_start, total_end, avg_change,
            avg_percent_change
        ])

    print tabulate(table)


rate_of_increase()
print
rate_of_increase(change_only = True)

summary()
summary(change_only = True)
