# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:53:34 2022

@author: TRO1COB
"""
from check_limits import battery_is_ok
if __name__ == '__main__':
  assert(battery_is_ok(-5, 60) is False)
  assert(battery_is_ok(46, 80) is False)
  assert(battery_is_ok(5, 19) is False)
  assert(battery_is_ok(28, 81) is False)
  assert(battery_is_ok(25, 50) is True)
  assert(battery_is_ok(-20, 9) is False)  
  print("All is Well!")
  
  
