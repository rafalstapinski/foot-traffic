import web
import pickle
from datetime import datetime

# db = web.database(dbn='sqlite', db='foot-traffic.db')
#
# sbuxs = db.select('locations', dict(chain=1), where='chain_id=$chain').list()
#
# sbux_stats = []
#
# for sbux in sbuxs:
#
#     sbux_stats = sbux_stats + db.select('stats', dict(venue_id=sbux.id), where='venue_id=$venue_id').list()

with open('sbux_stats.pickle', 'r') as f:
    sbux_stats = pickle.load(f)

stats = {}

for stat in sbux_stats:

    # if stat.venue_id in stats:
    #     stats[stat.venue_id][stat.]

    d = stat.date[:10]

    if stat.venue_id in stats:
        stats[stat.venue_id][d] = stat.visits_count
    else:
        stats[stat.venue_id] = {}
        stats[stat.venue_id][d] = stat.visits_count

a='2017-08-02'
b='2017-08-03'
c='2017-08-04'
d='2017-08-05'
e='2017-08-06'
f='2017-08-07'

a_avg = 0
b_avg = 0
c_avg = 0
d_avg = 0
e_avg = 0
f_avg = 0

for v in stats:

    # TODO: investigate why some dates are missing
    # Probably has to do with rate limiting

    if a in stats[v]:
        a_avg = a_avg + stats[v][a]
    if b in stats[v]:
        b_avg = b_avg + stats[v][b]
    if c in stats[v]:
        c_avg = c_avg + stats[v][c]
    if d in stats[v]:
        d_avg = d_avg + stats[v][d]
    if e in stats[v]:
        e_avg = e_avg + stats[v][e]
    if f in stats[v]:
        f_avg = f_avg + stats[v][f]

print b_avg - a_avg
# print c_avg - b_avg
# print d_avg - c_avg
print e_avg - d_avg
print f_avg - e_avg
