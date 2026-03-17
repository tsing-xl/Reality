import pyglet
from ..log4r import *

__version__ = '1.0'
__version_v2__ = (1, 0, 0)

class BaseWidget:
    def __init__(self, *kw) -> None:
        '''The basic structure of widgets. Call other widgets instead.'''
        # TODO: Complete the document.
        # Interface to display.
        self.interface = None
        self.__classname = __class__.__name__

        # The widget's coordinate in pyglet.
        self.x: int = 0
        self.y: int = 0

        # New features: Rendering Layer
        self.rendering_layer: any = None

        # Old features [Outdated]: Graphics batch
        self.graphics_batch: pyglet.graphics.Batch = None
    
    # --- These function need to be overwrite.
    def checkUpWidget(self) -> None: 
        '''Check up if exists at least 1 widget render. Without widget render, we can't draw anything.'''
        return

    def recomposeWidget(self) -> None:
        '''Recompose the widget if possible. Doesn't support rewrite widget's attribute via function argument.'''
        return
    
    def composeWidget(self) -> None:
        '''Compose the widget. As same as recomposeWidget. Possibly duplicated in further version.'''
        return self.recomposeWidget

    def removeWidget(self) -> None:
        '''Remove the widget from memory ant your interface. Can't promise safety but effective.'''
        return

    def logout(self, lvl: int = 0, text: str = '') -> None:
        '''Logs out what happens in the Widget class.'''
        return logout(f'{self.__classname}@{self}', lvl, text)
    