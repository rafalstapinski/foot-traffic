import requests
from config import *
import json
import web
import sys

db = web.database(dbn=DB.dbn, db=DB.db)

def add_chain(name):

    return db.insert('chains', name=name)

def first_run(chain_id):

    chain = db.select('chains', dict(id=chain_id), where='id=$id').first()

    top = 50
    left = -125
    right = -65
    bottom = 25

    for lat in range(bottom, top)[0::2]:
        for lng in range(left, right)[0::2]:

            url = API.url % ('venues/search', '&query=%s&ll=%s,%s' % (chain.name, lat, lng))

            r = requests.get(url).json()

            for venue in r['response']['venues']:
                print venue['id']
                if db.select('locations', dict(venue_id=venue['id']), where='id=$venue_id').first() is None:
                    db.insert('locations', id=venue['id'], chain_id=chain_id)

def norm_run(chain_id):

    chain = db.select('chains', dict(id=chain_id), where='id=$id').first()

    locations = db.select('locations', dict(chain_id=chain_id, where='chain_id = $chain_id')).list()

    for location in locations:

        url = API.url % ('venues/search', '&query=%s&ll=%s,%s' % (chain.name, location.lat, location.lng))

        r = requests.get(url).json()

        for venue in r['response']['venues']:

            db.insert('traffic', venue_id=venue['id'], traffic=venue['stats']['checkinsCount'], chain_id=chain_id)

cmd = sys.argv[1]

if cmd == 'setup_db':

    for q in DB.setup_sql:
        db.query(q)

elif cmd == 'add':
    chain_id = add_chain(sys.argv[2])
    first_run(chain_id)
