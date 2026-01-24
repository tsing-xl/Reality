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
from .consolelogs import consoleLogout
# from .exceptionhander import ExceptionHandler

__version = '1.1.0'
__version_v2__ = (1, 1, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Interface module version {__version}.')

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
            caption = interface_title, 
            resizable = False, 
            vsync = vsync, 
            file_drops = True, 
            # Invisible first before loading
            visible = False, 
        )
        

        self._w, self._h = width, height
        self._title = interface_title
        # self._toplevel_mode = False
        # self._vsync = vsync
        self._dropped_files: list = []

        self.composer = WidgetComposer(self)
        self.widget_handler = WidgetHandler()
        self.background = Background()

        self._bindHandler()
        self._window.set_visible(True)
    
    # ======== Internal methods ========
    
    def recompose(self) -> None:
        self.composer.recompose()
        self.widget_handler.recompose()
    
    # ======== Event handlers ========

    def _bindHandler(self) -> None:
        # Bind event handlers to the window
        self._window.set_handler('on_draw', self.interfaceDisplayHandler)
        self._window.set_handler('on_mouse_motion', self.mouseMotionHandler)
        self._window.set_handler('on_mouse_press', self.mouseClickHandler)
        self._window.set_handler('on_close', self.quitApplication)
        self._window.set_handler('on_drop_file', self.fileDropHandler)

    def mouseMotionHandler(self, x, y, dx, dy) -> None:
        '''Handle mouse motion by widget_handler.'''
        self.widget_handler.motionHandler(x, y)
    
    def mouseClickHandler(self, x, y, button, modifiers) -> None:
        '''Handle mouse click by widget_handler.'''
        self.widget_handler.clickHandler(x, y)
    
    def fileDropHandler(self, x, y, dropped_files: list) -> None:
        '''Handle file drop by widget_handler.'''
        self._dropped_files = dropped_files
    
    def interfaceDisplayHandler(self, *kw) -> None:
        self._window.clear()
        
        self.background.drawBackground()
        self.composer.draw()
    
    # ======== Application control ========
    def runApplication(self) -> None:
        # self._exc_handler = ExceptionHandler(app.run)
        self.logout(0, 'the code after runApplication will not be executed except the function returns a value or window quit.')
        # self._exc_handler.execute()
        app.run()

    def quitApplication(self) -> None:
        self.logout(0, 'Quitting application...')
        self._window.close()
    
    def logout(self, lvl: int = 0, text: str = '') -> None: consoleLogout(f'{__class__.__name__}@{self}', lvl, text)