import web
import pickle
import matplotlib.pyplot as plt

def weekly_stats():

    chains = pickle.load(open('stats_weekly.p', 'rb'))

    x_axis = [i for i in range(1, 10)]

    for chain in chains:
        loc_length = 0
        y_axis = [0 for _ in range(0, 10)]
        for stat in chains[chain]:
            if None in stat:
                loc_length += 1

        print '%s %d' % (chain, loc_length)



    # print chains['starbucks']


weekly_stats()
