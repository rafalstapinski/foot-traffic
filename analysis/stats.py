import web
import pickle
from tabulate import tabulate
import numpy as np
from scipy import stats

def rate_of_increase():

    chains = pickle.load(open('stats_weekly.p', 'rb'))

    x = [i for i in range(1, 10)]

    for chain in chains:

        if chain == 'costco':
            continue

        y = np.zeros(9)
        locations_count = 0

        for stat in chains[chain]:

            # TODO: Figure out better method to use None

            if None in stat or 0 in stat:
                continue

            y += np.asarray(stat)
            locations_count += 1

        unw_slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

        y /= locations_count

        w_slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

        print chain, unw_slope, w_slope

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


def summary():

    stats = pickle.load(open('stats_weekly.p', 'rb'))

    table = [[
        'chain name', 'location count', 'total checkins at start',
        'total checkins at end', 'avg location change', 'avg location % change'
    ]]

    for chain in stats:

        if chain == 'costco':
            continue

        locations_count = 0

        locations_count_change_only = 0

        total_start = 0
        total_end = 0

        total_start_change_only = 0
        total_end_change_only = 0

        avg_change = 0
        avg_percent_change = 0

        avg_change_change_only = 0
        avg_percent_change_change_only = 0

        for stat in stats[chain]:

            k = 0

            for z in stat:
                if z == None:
                    k += 1

            if k > 2:
                continue # closed down starbucks

            start = next(i for i in stat if i != None)
            end = next(i for i in reversed(stat) if i != None)

            if end == 0:
                continue

            locations_count += 1

            total_start += start
            total_end += end

            if start != end:

                locations_count_change_only += 1
                total_start_change_only += start
                total_end_change_only += end


        avg_change = float(total_end - total_start) / float(locations_count)
        avg_percent_change /= float(locations_count) / 100

        table.append([
            chain, locations_count, total_start, total_end, avg_change,
            avg_percent_change, locations_count_change_only,
            total_start_change_only, total_end_change_only,
            avg_change_change_only, avg_percent_change_change_only,
        ])

    print tabulate(table)


rate_of_increase()
