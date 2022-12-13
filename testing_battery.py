# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:53:34 2022

@author: TRO1COB
"""
from check_limits import battery_is_ok
if __name__ == '__main__':
  assert(battery_is_ok(-1, 50) is False)
  assert(battery_is_ok(46, 60) is False)
  assert(battery_is_ok(1, 19) is False)
  assert(battery_is_ok(28, 81) is False)
  assert(battery_is_ok(25, 70) is True)
  assert(battery_is_ok(-20, 9) is False)
  assert(battery_is_ok(100, 100) is False)  
  print("All is Well!")
  
  
