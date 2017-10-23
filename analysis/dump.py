import web
import pickle

def start_end():

    db = web.database(dbn='sqlite', db='../src/foot-traffic.db')

    chains = db.select('chains').list()
    stats = {}

    for chain in chains:

        stats[chain.name] = []

        locations = db.select('locations', dict(chain_id=chain.id), where='chain_id=$chain_id').list()

        for location in locations:
            start = db.select('stats', dict(venue_id=location.id), where='venue_id=$venue_id', order='date ASC', limit=1).first()
            end = db.select('stats', dict(venue_id=location.id), where='venue_id=$venue_id', order='date DESC', limit=1).first()

            stats[chain.name].append((start.visits_count, end.visits_count))

    pickle.dump(stats, open('stats.p', 'wb'))

def weekly():

    db = web.database(dbn='sqlite', db='../src/foot-traffic.db')

    chains = db.select('chains').list()

    stats = {}

    w_one = db.select('stats', where="date LIKE '%2017-07-29%'").list()
    w_two = db.select('stats', where="date LIKE '%2017-08-05%'").list()
    w_thr = db.select('stats', where="date LIKE '%2017-08-12%'").list()
    w_fou = db.select('stats', where="date LIKE '%2017-08-19%'").list()
    w_fiv = db.select('stats', where="date LIKE '%2017-08-26%'").list()
    w_six = db.select('stats', where="date LIKE '%2017-09-02%'").list()
    w_sev = db.select('stats', where="date LIKE '%2017-09-09%'").list()
    w_eig = db.select('stats', where="date LIKE '%2017-09-16%'").list()
    w_nin = db.select('stats', where="date LIKE '%2017-09-23%'").list()
    w_ten = db.select('stats', where="date LIKE '%2017-09-30%'").list()


    for chain in chains:

        stats[chain.name] = []

        locations = db.select('locations', dict(chain_id=chain.id), where='chain_id=$chain_id').list()

        for location in locations:

            a = next((v.checkins_count for v in w_one if v.venue_id == location.id), None)
            b = next((v.checkins_count for v in w_two if v.venue_id == location.id), None)
            c = next((v.checkins_count for v in w_thr if v.venue_id == location.id), None)
            d = next((v.checkins_count for v in w_fou if v.venue_id == location.id), None)
            e = next((v.checkins_count for v in w_fiv if v.venue_id == location.id), None)
            f = next((v.checkins_count for v in w_six if v.venue_id == location.id), None)
            g = next((v.checkins_count for v in w_sev if v.venue_id == location.id), None)
            h = next((v.checkins_count for v in w_eig if v.venue_id == location.id), None)
            i = next((v.checkins_count for v in w_nin if v.venue_id == location.id), None)
            j = next((v.checkins_count for v in w_ten if v.venue_id == location.id), None)

            stats[chain.name].append((a, b, c, d, e, f, g, h, i, j))

        sys.stdout.write('. ')

    pickle.dump(stats, open('stats_weekly.p', 'wb'))

weekly()
