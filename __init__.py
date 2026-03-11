from .interface import *
# [Outdated features] from .widgetcomposer import WidgetComposer
from .composer.widgetcomposer import *
# [Outdated features] from .widgethandler import WidgetHandler
from .handler.widgethandler import *
from .widgets import *
from .log4r import logout
from .background import *

# Possibly outdated features.
from .widgets import *

__version__ = '1.00.20 / APRIL139'
__version_v2__ = (1, 00, 20, 'APRIL139')

logout('Reality', 0, f'Reality UI built on pyglet. Version {__version__}.')

'''
Reality TODOs: 

 -------------------------------- New feature area --------------------------------
TODO: Add button textures in Button.
TODO: Add module Texturedwith custom button texture.
'''