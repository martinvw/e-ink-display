from openhab import OpenHAB
from screens import Heos1Screen
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

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

inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.BLACK)
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)
img.paste(inky_display.BLACK)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("fonts/icofont.ttf", 66)
# font = ImageFont.truetype(FredokaOne, 36)
message = "Hello, World!"
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)
draw.text((x, y), message, inky_display.WHITE, font)
inky_display.set_image(img)
inky_display.show()