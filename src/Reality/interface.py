from pyglet import window, app
from typing import Callable
from .widgetcomposer import WidgetComposer
from .widgethandler import WidgetHandler
from .background import Background
from .consolelogs import consoleLogout

__version = '1.1.0'
__version_v2__ = (1, 1, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Interface module version {__version}.')

class Interface:
    def __init__(
            self, 
            width: int = 700, 
            height: int = 350, 
            interface_title: str = 'Reality.', 
            vsync: bool = True, 
        ):

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
        self._toplevel_mode = False
        # self._vsync = vsync

        self.composer = WidgetComposer(self)
        self.widget_handler = WidgetHandler()
        # self.background = Background()

        self._bindHandler()
        self._window.set_visible(True)
    
    def _bindHandler(self) -> None:
        self._window.set_handler('on_draw', self.interfaceDisplayHandler)
        self._window.set_handler('on_mouse_motion', self.mouseMotionHandler)
        self._window.set_handler('on_mouse_press', self.mouseClickHandler)
        self._window.set_handler('on_close', self.quitApplication)
    
    def recompose(self) -> None:
        self.composer.recompose()
    
    def mouseMotionHandler(self, x, y, dx, dy) -> None:
        '''Handle mouse motion by widget_handler.'''
        self.widget_handler.mouseMotionHandler(x, y)
    
    def mouseClickHandler(self, x, y, button, modifiers) -> None:
        '''Handle mouse click by widget_handler.'''
        self.widget_handler.mouseClickHandler(x, y)
    
    def interfaceDisplayHandler(self, *kw) -> None:
        self._window.clear()
        
        self.background.drawBackground()
        self.composer.drawComposer()
    
    def runApplication(self) -> None:
        self.logout(0, 'the code after runApplication will not be executed except the function returns a value or window quit.')
        app.run()
    
    def quitApplication(self) -> None:
        self.logout(0, 'Quitting application...')
        self._window.close()
    
    def logout(self, lvl: int = 0, text: str = '') -> None: consoleLogout(f'{__class__.__name__}@{self}', lvl, text)