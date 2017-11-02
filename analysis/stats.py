import web
import pickle
from tabulate import tabulate

def to_csv():

    stats = pickle.load(open('stats.p', 'rb'))

    stats_file_str = 'chain,start,end,change,percent change\n'

    for chain in stats:
        for stat in stats[chain]:
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

            locations_count += 1

            total_start += start
            total_end += end

            change = end - start
            percent_change = float(change) / float(start)

            avg_change += change
            avg_percent_change += percent_change

        if locations_count != 0:  # oops costco

            avg_change /= float(locations_count)
            avg_percent_change /= float(locations_count) / 100

            table.append([
                chain, locations_count, total_start, total_end, avg_change,
                avg_percent_change
            ])

    print tabulate(table)


summary()
