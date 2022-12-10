# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:38:09 2022

@author: TRO1COB
"""

import thresholds as bt
def temperature_beyond_limit(temperature):
    if temperature < bt.TEMPERATURE_MIN or temperature > bt.TEMPERATURE_MAX:
        return True
    return False