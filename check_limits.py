
from check_temperature import *
from check_soc import *


def battery_is_ok(temperature, soc):
    battery_condition =False
    battery_temp= temperature_beyond_limit(temperature)
    battery_soc= soc_beyond_limit(soc)
    if (battery_temp and battery_soc):
        battery_condition = True
        return battery_condition
    return battery_condition
