
from check_temperature import *
from check_soc import *
from check_charge_rate import *

def battery_is_ok(temperature, soc, charge_rate):  
    if temperature < 0 or temperature > 45:
      print('Temperature is out of range!')
      return False
    elif soc < 20 or soc > 80:
      print('State of Charge is out of range!')
      return False
    elif charge_rate > 0.8:
      print('Charge rate is out of range!')
    if temperature_beyond_limit(temperature) or soc_beyond_limit(soc) or charge_rate_beyond_limit(charge_rate):
       return False
    return True
