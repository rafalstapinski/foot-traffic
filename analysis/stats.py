import web
import pickle

stats = pickle.load(open('stats.p', 'rb'))

for stat in stats['chipotle']:
    if stat[1] !=  0:
        print float((stat[1] - stat[0])) / float(stat[1])
