import pyglet

from ..log4r import logout
from typing import Callable
from ..interface import Interface
from ..metadata import Metadata

class __basewidget__: 
    def __init__(self, *kw):
        self._x = 0
        self._y = 0
        self._width: int = 0
        self._height: int = 0

        self._metadata: Metadata | None = None
    
    def recompose(self) -> None: 
        '''A function used to rebuild this widget. Need overwrite.'''
        return None
    
    def remove(self) -> None: 
        '''A function used to delete the widget in graphics to free memory and gpus. Need overwrite.'''
        return None

class Button(__basewidget__):
    def __init__(
            self, 
            interface: Interface | None = None, 
            x: int = 0, 
            y: int = 0, 
            width: int = 0, 
            height: int = 0, 
            text: str = '', 
            text_size: int = 12, 
            command: Callable | None = None, 
            # New features
            text_font: str | None = None,
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
        
        Button example:
            from Reality import Interface, Button

            inter = Interface()

            def hello():
                print('Hello, Reality!')

            button = Button(inter, x=450, y=5, width=200, height=30, text='Hello World', command=hello)

            inter.runApplication()
        '''

        # Initialize base widget
        super().__init__()

        # Can't place widget without interface
        # if interface is None: raise SyntaxError('require param composer which is not a Nonetype object.')

        # Store parameters
        self._x, self._y = x, y
        self._width, self._height = width, height
        self._text = text
        self._t_size = text_size
        self._command = command
        self._interface = interface

        # TODO: Font support
        self._font = text_font # Doesn't support yet.

        if self._command is None: self.logout(2, 'Command argument have been set to: None.')

        # self._disabled = False

        # Create button layers
        self._button_layer = pyglet.shapes.Rectangle(
            x = x, 
            y = y, 
            width = width, 
            height = height, 
            color = (0, 0, 0, 50), 
            batch = self._interface.composer.graphics_batch, 
        )

        # Create text layer
        self._text_layer = pyglet.text.Label(
            text, 
            x = x + width / 2, 
            y = y + height / 2, 
            anchor_x = 'center', 
            anchor_y = 'center', 
            font_size = self._t_size, 
            batch = self._interface.composer.text_batch, 
            font_name = self._font,
        )

        # Metadata for widget handler
        self._metadata = Metadata(
            x = self._x,
            y = self._y,
            width = self._width,
            height = self._height,
        )

        # Register this widget to widget handler
        # [Outdated features] self._interface.widget_handler.registerNewWidget(self, self._metadata.metadata)
        self._interface.handler.registerWidget(self)

    # Update elements (update-type)
    def updateText(self, new_text: str | None = None) -> None:
        '''Update the text displayed on the button.'''
        if new_text is None: 
            self.logout(3, 'Require string-kind object in new_text, got None.')
            return
        
        self._text_layer.text = new_text
        self._text = new_text # REMIND: Also update self._text that used to recompose widgets.
    
    def updateCommand(self, new_command: Callable | None = None) -> None:
        if new_command is None:
            self.logout(3, 'Require Callable object in new_command, got None.')
            return
        
        else:
            self._command = new_command
    
    # Event handler (ack-type)
    def command(self) -> None:
        if self._command is None or not callable(self._command):
            return self.logout(2, 'The argument command is None or not a callable object, so it will not be triggered.')
        self._command()
    
    def onMouseMotion(self, x: int, y: int) -> None:    
        if self._x <= x <= self._metadata.metadata_v2[2] and self._y <= y <= self._metadata.metadata_v2[3]:
            if self._button_layer.color != (0, 0, 0, 150):
                self._button_layer.color = (0, 0, 0, 150)
        else:
            if self._button_layer.color != (0, 0, 0, 50):
                self._button_layer.color = (0, 0, 0, 50)
    
    def onMouseClick(self, x: int, y: int) -> None:
        if self._x <= x <= self._metadata.metadata_v2[2] and self._y <= y <= self._metadata.metadata_v2[3]:
            self.command()
    
    # Rebuild / Remake type (build-type)
    def recompose(self):
        self.remove()
        
        self._button_layer = pyglet.shapes.Rectangle(
            x = self._x, 
            y = self._y, 
            width = self._width, 
            height = self._height, 
            color = (0, 0, 0, 50), 
            batch = self._interface.composer.graphics_batch, # May change in next versions
        )

        self._text_layer = pyglet.text.Label(
            self._text, 
            x = self._x + self._width / 2, 
            y = self._y + self._height / 2, 
            anchor_x = 'center', 
            anchor_y = 'center', 
            font_size = self._t_size, 
            batch = self._interface.composer.text_batch, # May change in next versions
            font_name = self._font,
        )

        # Register again
        self._interface.handler.registerWidget(self)

    def remove(self) -> None:
        '''Remove widgets and graphics safely and quickly.'''

        # self._composer.removeWidget()

        # To aviod multiple removal errors
        if self._button_layer is None or self._text_layer is None: return
        
        # Call pyglet delete methods
        self._button_layer.delete()
        self._text_layer.delete()

        # Set to None to prevent further access
        self._button_layer, self._text_layer = None, None
    
    def logout(self, lvl: int = 0, text: str = '') -> None: logout(f'{__class__.__name__}@{self}', lvl, text)

class Label(__basewidget__):
    def __init__(
            self, 
            interface: Interface | None = None,
            x: int = 0,
            y: int = 0,
            text: str = '',
            text_size: int = 12,
            text_color: tuple = (255, 255, 255, 255),
            text_font: str = None, 
        ) -> None:
        """
        The label widget is used to display text on the interface.
        These arguments are required:
        
         - x, y: The position of the label.
         - text: The text to be displayed.

        :param interface: The Interface object to which this widget belongs.
        :param x: The x position of the label.
        :param y: The y position of the label.
        :param text: The text to be displayed.
        :param text_size: The size of the text.
        :param text_color: Change the text color in RGBA format.

         * The label widget does not support interaction.

         Label example:
            from Reality import Interface, Label

            inter = Interface()

            label = Label(inter, x=100, y=100, text='Hello, Reality!', text_size=16, text_color=(255, 0, 0, 255))

            inter.runApplication()
        """
        super().__init__()

        self._x, self._y = x, y
        self._text = text
        self._interface = interface
        self._font_size = text_size
        self._color = text_color
        self._font = text_font
        
        self._widget = pyglet.text.Label(
            text, 
            x = x, 
            y = y, 
            font_size = text_size, 
            color = text_color, 
            batch = interface.composer.text_batch, # Uh, probably graphics batch?
            font_name = self._font, 
        )

        # Why a label need to be registered?
        # interface.handler.registerNewWidget(self, self._metadata)
    
    def updateTextElement(self, new_text: str) -> None:
        '''Update the text displayed on the label.'''
        if self._widget is None: return
        self._widget.text = new_text
    
    def recompose(self):
        self.remove()
        
        # Recompose the label
        self._widget = pyglet.text.Label(
            self._text, 
            x = self._x, 
            y = self._y, 
            font_size = self._font_size, 
            color = self._color, 
            batch = self._interface.composer.text_batch, # Uh, probably graphics batch?
            font_name = self._font, 
        )
    
    def remove(self) -> None:
        '''Remove widgets and graphics safely and quickly.'''

        # To aviod multiple removal errors
        if self._widget is None: return
        
        # Call pyglet delete methods
        self._widget.delete()

        # Set to None to prevent further access
        self._widget = None

class Cover(__basewidget__):
    def __init__(
            self, 
            interface: Interface | None = None,
            is_main_cover: bool = False, # If true, it will cover the whole interface, and x, y, width, height will be ignored.
            x: int = 0,
            y: int = 0,
            width: int = 0,
            height: int = 0,
            color: tuple = (0, 0, 0, 50), 
        ):
        '''
        Draw a cover widget on the interface.
        If is_main_cover is set to True, it will cover the whole interface, and x, y, width, height will be ignored.

        These arguments are required:
            - interface: The Interface object to which this widget belongs.
            - is_main_cover: If true, it will cover the whole interface.
            - x, y: The position of the cover widget.
            - width, height: The size of the cover widget.

        :param interface: The Interface object to which this widget belongs.
        :param is_main_cover: If true, it will cover the whole interface.
        :param x: The x position of the cover widget.
        :param y: The y position of the cover widget.
        :param width: The width of the cover widget.
        :param height: The height of the cover widget.

         * This cover widget does not support interaction.
        
        Cover example:
            from Reality import Interface, Cover

            inter = Interface()

            cover = Cover(inter, True)

            inter.runApplication()
        '''
        
        super().__init__()

        if interface is None: raise SyntaxError('require param composer which is not a Nonetype object.')
        
        self._interface = interface
        self._is_main_cover = is_main_cover
        self._interface = interface
        self._x: int = x
        self._y: int = y
        self._width, self._height = width, height
        self._color = color
        self._hidden_color = color[:-1] + (0, )

        self.recompose()
        
        self._metadata = (
            self._x, self._y, self._width, self._height, 
        ) # type: ignore
    
    def hiddenCover(self) -> None:
        '''Hide the under cover widget.'''
        if self._widget is None or self._is_main_cover: return
        
        if self._widget.color != self._hidden_color: self._widget.color = self._hidden_color
    
    def showCover(self) -> None:
        '''Show the under cover widget.'''
        if self._widget is None or self._is_main_cover: return
        
        if self._widget.color != self._color: self._widget.color = self._color
    
    def recompose(self):
        if self._is_main_cover:
            self._x, self._y = 20, 20
            self._width, self._height = self._interface._window.width - 40, self._interface._window.height - 40

            self._widget = pyglet.shapes.Rectangle(
                x = self._x, 
                y = self._y, 
                width = self._width, 
                height = self._height, 
                color = self._color, 
                batch = self._interface.composer.under_cover_batch, 
            )
        
        else:
            self._x, self._y = self._x, self._y
            self._width, self._height = self._width, self._height

            self._widget = pyglet.shapes.Rectangle(
                x = self._x, 
                y = self._y, 
                width = self._width, 
                height = self._height, 
                color = self._color, 
                batch = self._interface.composer.graphics_batch, 
            )
    
    def remove(self):
        if hasattr(self, '_widget'):
            self._widget.delete()
            del self._widget

class CheckBox(__basewidget__):
    def __init__(
            self, 
            interface: Interface | None = None,
            x: int = 0,
            y: int = 0,
            text: str = '',
            text_size: int = 12,
            is_checked: bool = False,
        ):
        super().__init__()

        if interface is None: raise SyntaxError('require param composer which is not a Nonetype object.')

        self._interface = interface
        self._x, self._y = x, y
        self._text = text
        self._text_size = text_size
        self._is_checked = is_checked

        # Build visual parts immediately so the checkbox appears when constructed
        self.recompose()

    def switchStatus(self) -> None:
        self._is_checked = not self._is_checked

        if self._check_box_upper_layer.color == (255, 255, 255, 100):
            self._check_box_upper_layer.color = (255, 255, 255, 0)
        
        else:
            self._check_box_upper_layer.color = (255, 255, 255, 100)
    
    def recompose(self):

        if hasattr(self, '_check_box'): self._check_box.remove()
        if hasattr(self, '_text_label'): self._text_label.remove()

        self._check_box = Button(
            interface = self._interface,
            x = self._x,
            y = self._y,
            width = 20,
            height = 20,
            text = '',
            command = self.switchStatus,
        )

        self._check_box_upper_layer = pyglet.shapes.Rectangle(
            x = self._x + 2,
            y = self._y + 2,
            width = 16,
            height = 16,
            color = (255, 255, 255, 100),
            batch = self._interface.composer.graphics_batch,
        )

        self._text_label = Label(
            interface = self._interface,
            x = self._x + 30,
            y = self._y + 5,
            text = self._text,
            text_size = self._text_size,
        )
    
    def remove(self):
        self._check_box.remove()
        del self._check_box_upper_layer
        self._text_label.remove()

class SlideBarHorizonal(__basewidget__):
    def __init__(
            self, 
            interface: Interface, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
        ):
        super().__init__()

        # if widget_frame is None: 
        #     self.logout(3, 'While you are using a slide bar, it must be binded with a WidgetFrame-like object. Or nothing will hanppened.')
    
    def logout(self, lvl: int = 0, text: str = '') -> None: logout(f'{__class__.__name__}@{self}', lvl, text)