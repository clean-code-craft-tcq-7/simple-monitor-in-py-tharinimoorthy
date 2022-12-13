
from check_temperature import *
from check_soc import *


def battery_is_ok(temperature, soc):  
    if temperature < 0 or temperature > 45:
      print('Temperature is out of range!')
      return False
    elif soc < 20 or soc > 80:
      print('State of Charge is out of range!')
      return False
   
    if temperature_beyond_limit(temperature) and soc_beyond_limit(soc):
       return False
    return True
