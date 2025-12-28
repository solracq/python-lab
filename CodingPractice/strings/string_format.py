'''
@author: Solrac
'''

import logging

log = logging.getLogger()

def str_fmt(log):
    name = 'abc '
    last_name = 'a'

    name2 = 'ds '
    last_name2 = 'ab'

    log.info("Starting the code")
    print("I was expecting {expected} not {actual}".format(expected = name+last_name, actual = name2+last_name2))
    

str_fmt(log)