import requests
from config import *
import json
import web

db = web.database(dbn='sqlite', db='alt-data.db')

# r = requests.get(API.url)

top = 50
left = -125
right = -65
bottom = 25

i = 0


# x = json.loads(re)
#
# for venue in x['response']['venues']:
#     print venue['verified'], venue['stats']['checkinsCount']
#
# lat, lng = 40, -74
# url = API.url % ('venues/search', '&query=costco&ll=%s,%s' % (lat, lng))
#
# r = requests.get(url).json()

# for venue in r['response']['venues']:

def add_chain(name):

    db.insert('chains', name=name)

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

            if r['response']['venues'] != []:
                db.insert('locations', chain=chain_id, lat=lat, lng=lng)
                print 'exists', lat, lng
            else:
                print '------', lat, lng

def norm_run(chain_id):

    chain = db.select('chains', dict(id=chain_id), where='id=$id').first()
    locations = db.select('locations', dict(chain=chain_id, where='chain=$chain_id')).list()

    for location in locations:

        url = API.url % ('venues/search', '&query=%s&ll=%s,%s' % (chain.name, location.lat, location.lng))

        r = requests.get(url).json()

        for venue in r['response']['venues']:

            db.insert('traffic', venue_id=venue['id'], traffic=venue['stats']['checkinsCount'], chain_id=chain_id)

# def first_run(venue_id):
#
#
# lat, lng = 48, -74
# url = API.url % ('venues/search', '&query=costco&ll=%s,%s' % (lat, lng))
#
# r = requests.get(url).json()

# if r['response']['venues'] != []:
#     db.insert('locations', )

# norm_run(1)
add_chain('buffalo wild wings')
first_run(3)
norm_run(1)
norm_run(2)
norm_run(3)
