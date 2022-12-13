# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:37:53 2022

@author: TRO1COB
"""

import thresholds as bt
def soc_beyond_limit(soc):
    if soc < bt.STATE_OF_CHARGE_MIN or soc > bt.STATE_OF_CHARGE_MAX:
        return True
    return False
