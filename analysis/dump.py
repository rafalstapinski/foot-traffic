import web
import pickle

db = web.database(dbn='sqlite', db='../src/foot-traffic.db')

chains = db.select('chains').list()
stats= {}

for chain in chains:

    stats[chain.name] = []

    locations = db.select('locations', dict(chain_id=chain.id), where='chain_id=$chain_id').list()

    for location in locations:
        start = db.select('stats', dict(venue_id=location.id), where='venue_id=$venue_id', order='date ASC', limit=1).first()
        end = db.select('stats', dict(venue_id=location.id), where='venue_id=$venue_id', order='date DESC', limit=1).first()

        stats[chain.name].append((start.visits_count, end.visits_count))

pickle.dump(stats, open('stats.p', 'wb'))
