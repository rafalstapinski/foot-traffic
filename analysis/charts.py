import web

db = web.database(dbn='sqlite', db='../src/foot-traffic.db')

stats = db.select('stats',
        dict(venue='448d1ab2f964a5204c341fe3'),
        where='venue_id = $venue').list()


print stats[84].checkins_count - stats[0].checkins_count
