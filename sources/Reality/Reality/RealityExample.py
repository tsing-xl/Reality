from interface import *
from widgets import *

def command() -> None: print('Clicked!')

inter = Interface(interface_title = 'Hello, curel world.')
button = Button(inter, 450, 10, 200, 30, 'Hello, world.', command = command)

inter.runApplication()