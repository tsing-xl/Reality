import pyglet
from ..log4r import *
from .widget_base import BaseWidget

class Label(BaseWidget):
    def __init__(
            self, 
            # Required a interface to display! 
            interface, 

            # Coordinate
            x: int, 
            y: int, 
            text: str = '',

            # Supports RGB and RGBA
            color: tuple | list = (255, 255, 255, 255), 

            # Font infomation
            font_name: str = None, 
            font_size: int = 12, 

            # Or:
            font: any = None, ) -> None: 
        '''A label widget is used to display texts and infomations. It supports various kinds of font style and sizes.'''
        
        super().__init__()
        
        # The interface
        self.interface = interface

        # Widget's coordinate
        self.x, self.y = x, y

        # Attribute
        self.text: str = str(self.text)
        self.color: tuple = color

        # Font family / style
        self.font_name: str = font_name
        self.font_size: int = int(font_size)
        self.font: any = None

        # Widget. strongly recommend you to avoid using the _widget.
        self._widget = None

        # Interface checkup
        self.checkUpWidget()
    
    def checkUpWidget(self):
        # Missing interface warnings
        if self.interface is None: self.logout(2, 'Attention: This label can\'t display without interface. Check your code if necessary!')

        # TODO: Supports FontLoader.
        # if self.font: 
        #     self.font_name, self.font_size = self.font.returnFontAttribute()
    
    def recomposeWidget(self):
        
        # Recompose the widget by the same arguments.
        self._widget = pyglet.text.Label(
            text = self.text, 
            x = self.x, y = self.y, 
            font_name = self.font_name, 
            font_size = self.font_size, 
            color = self.color, 

            # The graphics batch that label draws.
            batch = self.interface.composer.text_batch, 
        )
    
    def composeWidget(self):

        # As same as recomposeWidget.
        # TODO: Probably remove in next version.
        return self.recomposeWidget()
    
    def removeWidget(self):

        # Remove the widget by del. The gc collector will collect the rubbish later.
        # TODO: Better recollection method.
        if hasattr(self, '_widget'): del self._widget
        self._widget = None
    
    def logout(self, lvl: int = 0, text: str = '') -> None: return self.logout(f'{__class__.__name__}@{self}', lvl, text)