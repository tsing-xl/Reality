'''
The Interface module for Reality framework, 
Provides a Interface to create and manage application windows and UI components.

The interface in the base component of Reality framework.
'''

from pyglet import window, app
# from typing import Callable
from .composer.widgetcomposer import WidgetComposer
from .handler.widgethandler import WidgetHandler
from .background import Background
from .log4r import logout
# from .exceptionhander import ExceptionHandler

class Interface:
    def __init__(
            self, 
            width: int = 700, 
            height: int = 350, 
            interface_title: str = 'Reality.', 
            # Enable vysnc to enchance performance. (Limited frame to lower CPU usage)
            vsync: bool = True, 
        ):
        '''
        Interface class to create and manage the application window and UI components.
        The basic building block of Reality framework.
        Provides methods to run and quit the application, handle events, and manage widgets.

        For various UI components, we have already prepared them in widgets.py, 
        and then call example_widget(interface = your_interface, ... ) to create them.
        we will process them in WidgetHandler and WidgetComposer automatically.

        :param width: The width of the interface window.
        :param height: The height of the interface window.
        :param interface_title: The title of the interface window.
        :param vsync: Whether to enable vsync for performance enhancement.

        Interface Example:
        
        ```
        from Reality.interface import Interface

        interface = Interface(width = 800, height = 600, interface_title = 'My Reality App', vsync = True)

        interface.runApplication()
        ```

        * Hint: We also strongly recommend you to use Typing hints for better coding experience.
            - Such as: 
                count: int = 0
                name: str = 'John Doe'
                is_active: bool = True
                book_list: list = []
                ...

                And also:

                mutable_iterable_variable: list | tuple = [].
                Combine multiple types with | operator.
        
                Have fun in coding with Reality! -- Tsing.xl
        '''

        self._window = window.Window(
            width = width, 
            height = height, 

            # The caption means the title of the window.
            caption = interface_title, 
            resizable = False, 
            vsync = vsync, 
            file_drops = True, 

            # Window should be visible before completely loaded.
            visible = False, 
        )
        
        # !!!Attention!!! These are outdated features, enable them only in debug mode or compatible older version.
        # self._w, self._h = width, height
        # self._title = interface_title
        # self._toplevel_mode = False
        # self._vsync = vsync
        # self._dropped_files: list = []

        # ** These are new features: 
        self.width: int = width
        self.height: int = height
        self.title: str = interface_title

        # If interface is in toplevel mode, Only widgets and frame in toplevel receives user's input.
        self.is_in_toplevel_mode: bool = False

        # Enables vsync. This setting helps to improve the perfomance in pyglet.
        self.enable_vsync: bool = vsync

        # the composer of interface. Used to compose the widgets and display them on the window.
        self.composer = WidgetComposer(self)

        # The handler of interface. Deals with the user's interact.
        self.handler = WidgetHandler()

        # Outdated: self.widget_handler

        # The background of the window. Supports custom image.
        self.background = Background()

        # Bind the handlers.
        # [Outdated] self._bindHandler()
        self.bindHandler()

        # And finally, we can show the interface to users!
        self._window.set_visible(True)

        # FIXME: Attention: The animation of startup should delay for ~0.5s to call. The window won't display first.
    
    def recompose(self) -> None:

        # Recompose the composer and handler.
        self.composer.recompose()
        self.handler.recompose()

    def bindHandler(self) -> None:
        # Bind event handlers to the window.
        self._window.set_handler('on_draw', self.interfaceDisplayHandler)
        self._window.set_handler('on_mouse_motion', self.mouseMotionHandler)
        self._window.set_handler('on_mouse_press', self.mouseClickHandler)
        self._window.set_handler('on_close', self.quitApplication)
        self._window.set_handler('on_drop_file', self.fileDropHandler)
        # TODO: Add custom event handler.

    def mouseMotionHandler(self, x, y, dx, dy) -> None:
        '''Handle mouse motion by widget_handler.'''
        self.handler.motionHandler(x, y)
    
    def mouseClickHandler(self, x, y, button, modifiers) -> None:
        '''Handle mouse click by widget_handler.'''
        self.handler.clickHandler(x, y)
    
    def fileDropHandler(self, x, y, dropped_files: list) -> None:
        '''Handle file drop by widget_handler.'''
        # FIXME: Notification to special widgets.
        self._dropped_files = dropped_files
    
    def interfaceDisplayHandler(self, *kw) -> None:
        '''The display function for interface.'''
        # Before drawing, clear previous frame first.
        self._window.clear()

        # Draw the background first.
        self.background.drawBackground()

        # Let the composer draw.
        self.composer.draw()
    
    # ======== Application control ========
    def runApplication(self) -> None:
        # self._exc_handler = ExceptionHandler(app.run)
        # self._exc_handler.execute()
        app.run()
    
    # FIXME: Outdated features
    def setWindowSize(self, width: int, height: int) -> None:
        return self.outdatedWarnings('resizeWindow')
        self._w, self._h = width, height
        self._window.width, self._window.height = self._w, self._h
    
    def resizeWindow(
            self, 
            width: int, 
            height: int, 
    ) -> None:
        '''Resize window by calling self._window.set_size.'''
        self._window.set_size(width, height)

    def relocateWindow(
            self, 
            x: int = 0, 
            y: int = 0, 
    ) ->  None:
        '''Re locates the window.'''
        return

    def quitApplication(self) -> None:
        self.logout(0, 'Quitting application...')
        self._window.close()
    
    def logout(self, lvl: int = 0, text: str = '') -> None: 
        '''Prints the log of THIS class.'''
        logout(f'{__class__.__name__}@{self}', lvl, text)
    
    def outdatedWarnings(self, recommend_function = None) -> None: 
        '''Prints outdated warnings.
        
        Usage: 
        ```
        def outdated_function(self, *kw) -> None: 
            return self.outdatedWarning(self.foo)
            ...
            [Outdated code]
        ```
        '''
        self.logout(2, f'You are now using a outdated function. Try {recommend_function} instead. (This function will not executed)')