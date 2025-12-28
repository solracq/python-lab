'''
@author: Solrac
'''

import logging

log = logging.getLogger()

def str_fmt(log):
    name = 'Naomi '
    last_name = 'Q'

    name2 = 'Camelit '
    last_name2 = 'QP'

    log.info("Starting the code")
    print("I was expecting {expected} not {actual}".format(expected = name+last_name, actual = name2+last_name2))
    

str_fmt(log)