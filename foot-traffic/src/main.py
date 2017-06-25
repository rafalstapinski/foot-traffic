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



# re = '''{
# 	"meta": {
# 		"code": 200,
# 		"requestId": "594ea033351e3d7163000152"
# 	},
# 	"response": {
# 		"venues": [{
# 			"id": "4b782b4ff964a5208eb92ee3",
# 			"name": "Costco Wholesale",
# 			"contact": {
# 				"phone": "7322626300",
# 				"formattedPhone": "(732) 262-6300"
# 			},
# 			"location": {
# 				"address": "465 Route 70",
# 				"lat": 40.054683217498436,
# 				"lng": -74.15764236674016,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.054683217498436,
# 					"lng": -74.15764236674016
# 				}],
# 				"distance": 14752,
# 				"postalCode": "08723",
# 				"cc": "US",
# 				"city": "Brick Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["465 Route 70", "Brick Township, NJ 08723", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d1f6941735",
# 				"name": "Department Store",
# 				"pluralName": "Department Stores",
# 				"shortName": "Department Store",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/departmentstore_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": true,
# 			"stats": {
# 				"checkinsCount": 8063,
# 				"usersCount": 1740,
# 				"tipCount": 27
# 			},
# 			"url": "http:\/\/www.costco.com",
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"storeId": "",
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [{
# 				"id": "556a3897a7c8957d73d55980"
# 			}],
# 			"hasPerk": false
# 		}, {
# 			"id": "4c58baa1b05c1b8d3938d4b1",
# 			"name": "Costco Wholesale",
# 			"contact": {
# 				"phone": "7324810023",
# 				"formattedPhone": "(732) 481-0023"
# 			},
# 			"location": {
# 				"address": "2361 Hwy 66",
# 				"crossStreet": "Seaview Square Mall",
# 				"lat": 40.233269595244,
# 				"lng": -74.04560923576355,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.233269595244,
# 					"lng": -74.04560923576355
# 				}],
# 				"distance": 26255,
# 				"postalCode": "07712",
# 				"cc": "US",
# 				"city": "Ocean Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["2361 Hwy 66 (Seaview Square Mall)", "Ocean Township, NJ 07712", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d1f6941735",
# 				"name": "Department Store",
# 				"pluralName": "Department Stores",
# 				"shortName": "Department Store",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/departmentstore_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": true,
# 			"stats": {
# 				"checkinsCount": 7144,
# 				"usersCount": 1553,
# 				"tipCount": 27
# 			},
# 			"url": "http:\/\/www.costco.com",
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 1,
# 				"summary": "One other person is here",
# 				"groups": [{
# 					"type": "others",
# 					"name": "Other people here",
# 					"count": 1,
# 					"items": []
# 				}]
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [{
# 				"id": "556a3897a7c8957d73d55980"
# 			}],
# 			"hasPerk": false
# 		}, {
# 			"id": "4df7676262e141c90764777a",
# 			"name": "Costco Wholesale",
# 			"contact": {
# 				"phone": "7326174340",
# 				"formattedPhone": "(732) 617-4340"
# 			},
# 			"location": {
# 				"address": "18 Route 9 North",
# 				"crossStreet": "Texas Rd.",
# 				"lat": 40.36155786004381,
# 				"lng": -74.30356262959164,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.36155786004381,
# 					"lng": -74.30356262959164
# 				}],
# 				"distance": 47816,
# 				"postalCode": "07751",
# 				"cc": "US",
# 				"city": "Morganville",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["18 Route 9 North (Texas Rd.)", "Morganville, NJ 07751", "United States"]
# 			},
# 			"categories": [{
# 				"id": "52e816a6bcbc57f1066b7a54",
# 				"name": "Warehouse Store",
# 				"pluralName": "Warehouse Stores",
# 				"shortName": "Warehouse Store",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/default_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": true,
# 			"stats": {
# 				"checkinsCount": 7349,
# 				"usersCount": 1528,
# 				"tipCount": 26
# 			},
# 			"url": "http:\/\/www.costco.com",
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [{
# 				"id": "556a3897a7c8957d73d55980"
# 			}],
# 			"hasPerk": false
# 		}, {
# 			"id": "4da1b8189aa4721eab3f001a",
# 			"name": "Costco Wholesale",
# 			"contact": {
# 				"phone": "7323353800",
# 				"formattedPhone": "(732) 335-3800"
# 			},
# 			"location": {
# 				"address": "2835 Route 35 N",
# 				"crossStreet": "at Miller Ave.",
# 				"lat": 40.41920101674462,
# 				"lng": -74.17074374476631,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.41920101674462,
# 					"lng": -74.17074374476631
# 				}],
# 				"distance": 48870,
# 				"postalCode": "07730",
# 				"cc": "US",
# 				"city": "Hazlet",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["2835 Route 35 N (at Miller Ave.)", "Hazlet, NJ 07730", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d1f6941735",
# 				"name": "Department Store",
# 				"pluralName": "Department Stores",
# 				"shortName": "Department Store",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/departmentstore_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": true,
# 			"stats": {
# 				"checkinsCount": 7349,
# 				"usersCount": 1608,
# 				"tipCount": 24
# 			},
# 			"url": "http:\/\/www.costco.com",
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 1,
# 				"summary": "One other person is here",
# 				"groups": [{
# 					"type": "others",
# 					"name": "Other people here",
# 					"count": 1,
# 					"items": []
# 				}]
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [{
# 				"id": "556a3897a7c8957d73d55980"
# 			}],
# 			"hasPerk": false
# 		}, {
# 			"id": "4b7da620f964a5202bcc2fe3",
# 			"name": "Costco Wholesale",
# 			"contact": {
# 				"phone": "6092422011",
# 				"formattedPhone": "(609) 242-2011"
# 			},
# 			"location": {
# 				"address": "245 Stafford Park Blvd",
# 				"lat": 39.707882245158196,
# 				"lng": -74.28752563213806,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 39.707882245158196,
# 					"lng": -74.28752563213806
# 				}],
# 				"distance": 40757,
# 				"postalCode": "08050",
# 				"cc": "US",
# 				"city": "Stafford Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["245 Stafford Park Blvd", "Stafford Township, NJ 08050", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d1f6941735",
# 				"name": "Department Store",
# 				"pluralName": "Department Stores",
# 				"shortName": "Department Store",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/departmentstore_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": true,
# 			"stats": {
# 				"checkinsCount": 4194,
# 				"usersCount": 843,
# 				"tipCount": 7
# 			},
# 			"url": "http:\/\/www.costco.com",
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 2,
# 				"summary": "2 people are here",
# 				"groups": [{
# 					"type": "others",
# 					"name": "Other people here",
# 					"count": 2,
# 					"items": []
# 				}]
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [{
# 				"id": "556a3897a7c8957d73d55980"
# 			}],
# 			"hasPerk": false
# 		}, {
# 			"id": "4ed11829b634dd299251ac10",
# 			"name": "Costco Gasoline",
# 			"contact": {
# 				"phone": "7322626300",
# 				"formattedPhone": "(732) 262-6300"
# 			},
# 			"location": {
# 				"address": "465 State Hig. 70",
# 				"lat": 40.055376139458986,
# 				"lng": -74.15866872246505,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.055376139458986,
# 					"lng": -74.15866872246505
# 				}],
# 				"distance": 14863,
# 				"postalCode": "08723",
# 				"cc": "US",
# 				"city": "Brick Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["465 State Hig. 70", "Brick Township, NJ 08723", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d113951735",
# 				"name": "Gas Station",
# 				"pluralName": "Gas Stations",
# 				"shortName": "Gas Station",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/gas_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 1532,
# 				"usersCount": 288,
# 				"tipCount": 7
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "4ec7d20fb634b2fd74d02e2e",
# 			"name": "Costco Gas",
# 			"contact": {},
# 			"location": {
# 				"lat": 40.36169196219353,
# 				"lng": -74.30424441407452,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.36169196219353,
# 					"lng": -74.30424441407452
# 				}],
# 				"distance": 47860,
# 				"postalCode": "07751",
# 				"cc": "US",
# 				"city": "Morganville",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Morganville, NJ 07751", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d113951735",
# 				"name": "Gas Station",
# 				"pluralName": "Gas Stations",
# 				"shortName": "Gas Station",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/gas_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 2637,
# 				"usersCount": 400,
# 				"tipCount": 6
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "4c8d22c2509e3704f88e3955",
# 			"name": "Costco Gas Station",
# 			"contact": {
# 				"phone": "7324810023",
# 				"formattedPhone": "(732) 481-0023"
# 			},
# 			"location": {
# 				"address": "2361 State Route 66",
# 				"crossStreet": "Seaview Square Mall",
# 				"lat": 40.233514,
# 				"lng": -74.04675056666666,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.233514,
# 					"lng": -74.04675056666666
# 				}],
# 				"distance": 26297,
# 				"postalCode": "07712",
# 				"cc": "US",
# 				"city": "Ocean Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["2361 State Route 66 (Seaview Square Mall)", "Ocean Township, NJ 07712", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d113951735",
# 				"name": "Gas Station",
# 				"pluralName": "Gas Stations",
# 				"shortName": "Gas Station",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/gas_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 2528,
# 				"usersCount": 363,
# 				"tipCount": 17
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "4d5d4d563f92236ac057e81d",
# 			"name": "Costco Snack Bar",
# 			"contact": {},
# 			"location": {
# 				"lat": 40.054643690207314,
# 				"lng": -74.15798639722296,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.054643690207314,
# 					"lng": -74.15798639722296
# 				}],
# 				"distance": 14776,
# 				"postalCode": "08723",
# 				"cc": "US",
# 				"city": "Brick Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Brick Township, NJ 08723", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d1c7941735",
# 				"name": "Snack Place",
# 				"pluralName": "Snack Places",
# 				"shortName": "Snacks",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/food\/snacks_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 105,
# 				"usersCount": 33,
# 				"tipCount": 2
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "54087fab498ea939fdc56a2c",
# 			"name": "Costco Pharmacy",
# 			"contact": {},
# 			"location": {
# 				"address": "2361 Hwy 66",
# 				"lat": 40.233773,
# 				"lng": -74.04577,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.233773,
# 					"lng": -74.04577
# 				}],
# 				"distance": 26313,
# 				"postalCode": "07712",
# 				"cc": "US",
# 				"city": "Ocean Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["2361 Hwy 66", "Ocean Township, NJ 07712", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d10f951735",
# 				"name": "Pharmacy",
# 				"pluralName": "Pharmacies",
# 				"shortName": "Pharmacy",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/pharmacy_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 13,
# 				"usersCount": 5,
# 				"tipCount": 1
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "502e498ce4b0c65b4a377cca",
# 			"name": "Costco tires",
# 			"contact": {},
# 			"location": {
# 				"lat": 40.233418903497444,
# 				"lng": -74.04533999351005,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.233418903497444,
# 					"lng": -74.04533999351005
# 				}],
# 				"distance": 26269,
# 				"postalCode": "07753",
# 				"cc": "US",
# 				"city": "Neptune Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Neptune Township, NJ 07753", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d124951735",
# 				"name": "Automotive Shop",
# 				"pluralName": "Automotive Shops",
# 				"shortName": "Automotive",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/automotive_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 16,
# 				"usersCount": 6,
# 				"tipCount": 0
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "4eef63a9d3e3246bdd7e8156",
# 			"name": "Costco Eye Care",
# 			"contact": {},
# 			"location": {
# 				"address": "Costco",
# 				"lat": 40.233468924648086,
# 				"lng": -74.0458506101517,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.233468924648086,
# 					"lng": -74.0458506101517
# 				}],
# 				"distance": 26280,
# 				"postalCode": "07712",
# 				"cc": "US",
# 				"city": "Neptune Township",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Costco", "Neptune Township, NJ 07712", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4d954afda243a5684865b473",
# 				"name": "Optical Shop",
# 				"pluralName": "Optical Shops",
# 				"shortName": "Optical",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/building\/medical_opticalshop_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 18,
# 				"usersCount": 9,
# 				"tipCount": 0
# 			},
# 			"venueRatingBlacklisted": true,
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "52d16b5e11d257eb11be1734",
# 			"name": "costco gas",
# 			"contact": {},
# 			"location": {
# 				"lat": 39.7077988513523,
# 				"lng": -74.28636820918793,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 39.7077988513523,
# 					"lng": -74.28636820918793
# 				}],
# 				"distance": 40705,
# 				"cc": "US",
# 				"city": "Staffordville",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Staffordville, NJ", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d113951735",
# 				"name": "Gas Station",
# 				"pluralName": "Gas Stations",
# 				"shortName": "Gas Station",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/gas_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 143,
# 				"usersCount": 35,
# 				"tipCount": 0
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "507984f0e4b07018b657a77b",
# 			"name": "Costco Tire Center",
# 			"contact": {},
# 			"location": {
# 				"lat": 40.36141124490129,
# 				"lng": -74.30323605964524,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.36141124490129,
# 					"lng": -74.30323605964524
# 				}],
# 				"distance": 47788,
# 				"postalCode": "07751",
# 				"cc": "US",
# 				"city": "Morganville",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Morganville, NJ 07751", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d124951735",
# 				"name": "Automotive Shop",
# 				"pluralName": "Automotive Shops",
# 				"shortName": "Automotive",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/automotive_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 9,
# 				"usersCount": 8,
# 				"tipCount": 0
# 			},
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "4fef5e09e4b0bfd1e5d783e1",
# 			"name": "Costco Break Room",
# 			"contact": {},
# 			"location": {
# 				"lat": 40.361545778683904,
# 				"lng": -74.30225634627618,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.361545778683904,
# 					"lng": -74.30225634627618
# 				}],
# 				"distance": 47755,
# 				"postalCode": "07751",
# 				"cc": "US",
# 				"city": "Morganville",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Morganville, NJ 07751", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d128941735",
# 				"name": "Cafeteria",
# 				"pluralName": "Cafeterias",
# 				"shortName": "Cafeteria",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/education\/cafeteria_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 6,
# 				"usersCount": 4,
# 				"tipCount": 0
# 			},
# 			"venueRatingBlacklisted": true,
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "51f85dfe498ed18e066913d2",
# 			"name": "Costco Wholesale Club Backlot",
# 			"contact": {},
# 			"location": {
# 				"address": "Route 35",
# 				"crossStreet": "Miller Ave",
# 				"lat": 40.421345,
# 				"lng": -74.169413,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.421345,
# 					"lng": -74.169413
# 				}],
# 				"distance": 49064,
# 				"postalCode": "07730",
# 				"cc": "US",
# 				"city": "Hazlet",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Route 35 (Miller Ave)", "Hazlet, NJ 07730", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4c38df4de52ce0d596b336e1",
# 				"name": "Parking",
# 				"pluralName": "Parking",
# 				"shortName": "Parking",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/building\/parking_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": false,
# 			"stats": {
# 				"checkinsCount": 3,
# 				"usersCount": 3,
# 				"tipCount": 0
# 			},
# 			"venueRatingBlacklisted": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [],
# 			"hasPerk": false
# 		}, {
# 			"id": "4baf885df964a520e4073ce3",
# 			"name": "CVS\/pharmacy",
# 			"contact": {
# 				"phone": "6099701225",
# 				"formattedPhone": "(609) 970-1225",
# 				"twitter": "cvs_extra"
# 			},
# 			"location": {
# 				"address": "Route 9 & Texas Road",
# 				"lat": 40.363088204512906,
# 				"lng": -74.30557359997765,
# 				"labeledLatLngs": [{
# 					"label": "display",
# 					"lat": 40.363088204512906,
# 					"lng": -74.30557359997765
# 				}],
# 				"distance": 48052,
# 				"postalCode": "08857",
# 				"cc": "US",
# 				"city": "Old Bridge",
# 				"state": "NJ",
# 				"country": "United States",
# 				"formattedAddress": ["Route 9 & Texas Road", "Old Bridge, NJ 08857", "United States"]
# 			},
# 			"categories": [{
# 				"id": "4bf58dd8d48988d10f951735",
# 				"name": "Pharmacy",
# 				"pluralName": "Pharmacies",
# 				"shortName": "Pharmacy",
# 				"icon": {
# 					"prefix": "https:\/\/ss3.4sqi.net\/img\/categories_v2\/shops\/pharmacy_",
# 					"suffix": ".png"
# 				},
# 				"primary": true
# 			}],
# 			"verified": true,
# 			"stats": {
# 				"checkinsCount": 1507,
# 				"usersCount": 511,
# 				"tipCount": 2
# 			},
# 			"url": "http:\/\/cvs.com\/extracare",
# 			"allowMenuUrlEdit": true,
# 			"beenHere": {
# 				"lastCheckinExpiredAt": 0
# 			},
# 			"specials": {
# 				"count": 0,
# 				"items": []
# 			},
# 			"storeId": "CVS 2547",
# 			"hereNow": {
# 				"count": 0,
# 				"summary": "Nobody here",
# 				"groups": []
# 			},
# 			"referralId": "v-1498325043",
# 			"venueChains": [{
# 				"id": "556f5631bd6a75a99036ab9b"
# 			}],
# 			"hasPerk": false
# 		}]
# 	}
# }'''



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

norm_run(1)
