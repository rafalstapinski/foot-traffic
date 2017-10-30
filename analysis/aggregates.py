#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""aggregates.py: a collection of utilities for computing aggregates"""

from datetime import datetime
from datetime import timedelta
import json

import web


def _aggregate_query(start_date=None, end_date=datetime.now()):

    if start_date is None:
        start_date = end_date - timedelta(days=354)


    start_date_string = start_date.strftime('%Y-%m-%d')
    end_date_string = end_date.strftime('%Y-%m-%d')


    aggregate_query = ("""SELECT chains.name AS chain_name, 
                                SUM(stats.checkins_count) AS num_checkins, 
                                SUM(stats.users_count) AS num_users, 
                                SUM(stats.tip_count), 
                                SUM(stats.visits_count) AS num_visits
                            FROM stats
                            INNER JOIN chains
                                ON stats.id = chains.id
                            WHERE stats.date >= '{start_date}' AND stats.date <= '{end_date}'
                                GROUP BY chains.id
                                ORDER BY num_visits DESC, num_users DESC, num_checkins DESC;""").format(start_date=start_date_string, end_date=end_date_string)
    print(aggregate_query)
    return aggregate_query



def get_q3_aggregates(db_source='../src/foot-traffic.db', start_date=None, num_weeks=9):

    database = web.database(dbn='sqlite', db=db_source)

    if start_date is None:
        start_date = datetime.strptime('2017-07-29', '%Y-%m-%d')

    date_iterator = start_date

    for i in range(num_weeks):
        range_end = date_iterator + timedelta(days=7)

        query = _aggregate_query(start_date=date_iterator, end_date=range_end)

        aggregates = database.query(query)

        print(aggregates)

        for aggregate in aggregates:
            print(aggregate)

        date_iterator = range_end


def get_all_aggregated(db_source='../src/foot-traffic.db'):

    database = web.database(dbn='sqlite', db=db_source)

    query = _aggregate_query()

    aggregates = database.query(query)

    for aggregate in aggregates:
        print(json.dumps(aggregate, indent=4))




get_all_aggregated()
