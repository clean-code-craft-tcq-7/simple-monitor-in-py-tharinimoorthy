# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:37:15 2022

@author: TRO1COB
"""
import thresholds as bt
def charge_rate_beyond_limit(charge_rate):
    if charge_rate > bt.CHAGE_RATE_MAX:
        
        return True
    return False

