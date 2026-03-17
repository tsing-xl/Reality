import pyglet
from ..log4r import *
from .widget_base import BaseWidget
from .widget_texture import ImageTexture
from ..interface import Interface
from ..metadata import Metadata

from typing import Callable

class Label(BaseWidget):
    def __init__(
            self, 
            # Required a interface to display! 
            interface: Interface, 

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

        self.__classname = __class__.__name__
        
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

class Cover(BaseWidget):
    def __init__(
            self, 

            # Also, require a interface to display.
            interface: Interface, 

            # Location infomation for widget.
            x: int, 
            y: int, 
            width: int, 
            height: int, 

            # The color cover display. Default is 0,0,0,50.
            color: tuple = (0, 0, 0, 50), 
    ) -> None:
        '''A Cover is used to cover some unimportant elements or hide the loading progress.'''

        self.__classname = __class__.__name__
        
        self.interface = interface

        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height

        self.color = color

        self._widget = None
    
    def recomposeWidget(self):
        self._widget = pyglet.shapes.Rectangle(
            x = self.x, 
            y = self.y, 
            width = self.width, 
            height = self.height, 
            color = self.color, 
            batch = self.interface.composer.graphics_batch, 
        )
    
    def removeWidget(self):
        if hasattr(self, '_widget'): del self._widget

class Button(BaseWidget):
    def __init__(
            self, 

            # The interface.
            interface: Interface | None = None, 

            # The location and size.
            x: int = 0, 
            y: int = 0, 
            width: int = 0, 
            height: int = 0, 

            # What to display on the button.
            text: str = '', 
            text_size: int = 12, 
            text_font: str | None = None, 

            # When the button clicks, what should the button do.
            command: Callable | None = None, 
            ):
        '''
        The button widget is used to create clickable buttons on the interface.
        These arguments are required:
            - x, y: The position of the button.
            - width, height: The size of the button.
        
        :param interface: The Interface object to which this widget belongs.
        :param x: The x position of the button.
        :param y: The y position of the button.
        :param width: The width of the button.
        :param height: The height of the button.
        :param text: The text displayed on the button.
        :param text_size: The size of the text on the button.
        :param command: The function to be called when the button is clicked.
        :param text_font: The font to be used for the button text.

        * This button widget supports mouse hover and click interactions.
        '''

        # Initialize base widget
        super().__init__()

        self.__classname = __class__.__name__

        # Can't place widget without interface
        # if interface is None: raise SyntaxError('require param composer which is not a Nonetype object.')

        # Inteface
        self.interface: Interface = interface

        # Location
        self.x: int = x
        self.y: int = y

        # Size
        self.width: int = width
        self.height: int = height

        # Text display
        self.text: str = text

        self.text_font: str = text_font
        self.text_size: int = text_size

        # Command
        self.command = command

        # Metadata for widget handler
        self.metadata = Metadata(
            x = self.x,
            y = self.y,
            width = self.width,
            height = self.height,
        )

        # Register this widget to widget handler
        # [Outdated features] self._interface.widget_handler.registerNewWidget(self, self._metadata.metadata)
        self.interface.handler.registerWidget(self)

        self.text_layer, self.button_layer = None, None

        self.recomposeWidget()

    # Update elements (update-type)
    def updateText(self, new_text: str | None = None) -> None:
        '''Update the text displayed on the button.'''
        if new_text is None: 
            self.logout(3, 'Require string-kind object in new_text, got None.')
            return
        
        self.text_layer.text = new_text
        self.text = new_text # TODO: Also update self._text that used to recompose widgets.
    
    def updateCommand(self, new_command: Callable | None = None) -> None:
        if new_command is None:
            self.logout(3, 'Require Callable object in new_command, got None.')
            return
        
        else:
            self.command = new_command
    
    # Event handler (ack-type)
    def executeCommand(self) -> None:
        if self.command is None or not callable(self.command):
            return self.logout(2, 'The argument command is None or not a callable object, so it will not be triggered.')
        self.command()
    
    def onMouseMotion(self, x: int, y: int) -> None:    
        # TODO: Write comments here.
        if self.x <= x <= self.metadata.metadata_v2[2] and self.y <= y <= self.metadata.metadata_v2[3]:
            if self.button_layer.color != (0, 0, 0, 150):
                self.button_layer.color = (0, 0, 0, 150)
        else:
            if self.button_layer.color != (0, 0, 0, 50):
                self.button_layer.color = (0, 0, 0, 50)
    
    def onMouseClick(self, x: int, y: int) -> None:
        # TODO: Also write comments here.
        if self.x <= x <= self.metadata.metadata_v2[2] and self.y <= y <= self.metadata.metadata_v2[3]:
            self.executeCommand()
    
    # Rebuild / Remake type (build-type)
    def recomposeWidget(self):
        self.removeWidget()
        
        self.button_layer = pyglet.shapes.Rectangle(
            x = self.x, 
            y = self.y, 
            width = self.width, 
            height = self.height, 
            color = (0, 0, 0, 50), 
            batch = self.interface.composer.graphics_batch, # May change in next versions
        )

        self.text_layer = pyglet.text.Label(
            self.text, 
            x = self.x + self.width / 2, 
            y = self.y + self.height / 2, 
            anchor_x = 'center', 
            anchor_y = 'center', 
            font_size = self.text_size, 
            batch = self.interface.composer.text_batch, # May change in next versions
            font_name = self.text_font,
        )

        # Register again
        self.interface.handler.registerWidget(self)

    def removeWidget(self) -> None:
        '''Remove widgets and graphics safely and quickly.'''

        # self._composer.removeWidget()

        # To aviod multiple removal errors
        if self.button_layer is None or self.text_layer is None: return
        
        # Call pyglet delete methods
        self.button_layer.delete()
        self.text_layer.delete()

        # Set to None to prevent further access
        self.button_layer, self.text_layer = None, None

class CheckBox(BaseWidget):
    def __init__(
            self, 

            # Interface.
            interface: Interface | None = None,

            # Location.
            x: int = 0,
            y: int = 0,

            # Text info.
            text: str = '',
            text_size: int = 12,

            # Special param: If checkbox is already pressed.
            is_checked: bool = False,
        ) -> None:
        # TODO: Rewrite it
        super().__init__()

        self.__classname = __class__.__name__

        if interface is None: raise SyntaxError('require param composer which is not a Nonetype object.')

        self.interface = interface
        self.x: int = x, 
        self.y: int = y
        self.text: str = text
        self.text_size: int = text_size
        self.is_checked: bool = is_checked

        # Build visual parts immediately so the checkbox appears when constructed
        self.recomposeWidget()

    def switchStatus(self) -> None:
        self.is_checked = not self.is_checked

        if self.check_box_upper_layer.color == (255, 255, 255, 100):
            self.check_box_upper_layer.color = (255, 255, 255, 0)
        
        else:
            self.check_box_upper_layer.color = (255, 255, 255, 100)
    
    def recomposeWidget(self):
        self.removeWidget()

        self.check_box = Button(
            interface = self.interface,
            x = self.x,
            y = self.y,
            width = 20,
            height = 20,
            text = '',
            command = self.switchStatus,
        )

        self.check_box_upper_layer = pyglet.shapes.Rectangle(
            x = self.x + 2,
            y = self.y + 2,
            width = 16,
            height = 16,
            color = (255, 255, 255, 100),
            batch = self.interface.composer.graphics_batch,
        )

        self.text_label = Label(
            interface = self.interface,
            x = self.x + 30,
            y = self.y + 5,
            text = self.text,
            text_size = self.text_size,
        )
    
    def removeWidget(self):
        self.check_box.remove()
        del self.check_box_upper_layer
        self.text_label.remove()

class BluredCover(BaseWidget):
    def __init__(self, 
            interface: Interface | None = None,
            x: int = 0,
            y: int = 0, 
            width: int = 0, 
            height: int = 0, 
            textures: ImageTexture = None, 
        ) -> None:
        super().__init__()

        # Interface.
        self.interface = interface

        # Metadata.
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height

        # The texture of the cover.
        self.textures = textures
        self.recomposeWidget()

    def recomposeWidget(self):
        # Load image from cache.
        self.blured_image = pyglet.image.load(self.textures.filename)

        # Create widget.
        self.widget = pyglet.sprite.Sprite(
            self.blured_image, 
            x = self.x, 
            y = self.y, 
            batch = self.interface.composer.graphics_batch, 
        )
    
    def updateTexture(self, new_texture: ImageTexture) -> None:
        self.textures = new_texture
    
    def removeWidget(self):
        if hasattr(self, 'widget'): self.widget.delete()
        del self.widget