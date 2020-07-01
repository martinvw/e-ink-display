from openhab import OpenHAB
from screens import Heos1Screen

base_url = 'http://192.168.1.20:5080/rest'
openhab = OpenHAB(base_url)

# fetch a single item
item = openhab.get_item('LocalWeatherAndForecastForecastHours06IconId')

print(item.state)

item = openhab.get_item('HEOS1Control')

print(item.state)

item = openhab.get_item('HEOS1Album')

print(item.state)

item = openhab.get_item('HEOS1Artist')

print(item.state)

# turn a switch on
# item.command('OFF')

screen = Heos1Screen(openhab)

print(screen.button_2_label())
print(screen.button_4_label())