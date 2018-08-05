'''
Various utility functions
'''

import datetime


def get_current_ts():
    '''
    Retrieve UTC unix timestamp
    '''
    return int(datetime.datetime.utcnow().timestamp())


def extract_at_idx(lst, idx=0):
    '''
    Given a list of lists extracts idx-th element
    '''

    return [x[idx] for x in lst]


def row_to_dict(rows):
    '''
    Turn rows to list of dicts
    '''

    if not rows:
        return []

    return [dict(r) for r in rows]
