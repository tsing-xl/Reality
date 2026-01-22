from typing import Callable
from .consolelogs import consoleLogout
from threading import Thread

__version__ = '1.0.0'
__version_v2__ = (1, 0, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Widgethandler module version {__version__}.')

class WidgetHandler:
    def __init__(self):
        # TODO: Get better performance by some *tricks*
        self._widget_self_list: list | tuple = []
        self._widget_metadata_list: list | tuple = []

        # self._mouse_motion_thread = Thread(target=self._mouseMotionHandlerThread, daemon=True)
        # self._mouse_motion_thread.start()
    
    def registerNewWidget(self, widget_self, widget_metadata: tuple) -> None:
        self._widget_self_list.append(widget_self)
        self._widget_metadata_list.append(widget_metadata)
    
    def mouseMotionHandler(self, x, y):
        for index in self._widget_self_list: index.onMouseMotion(x, y)
        
    def mouseClickHandler(self, x, y) -> None:
        for index in self._widget_self_list: index.onMouseClick(x, y)
    
    def frozen(self) -> None:
        self._widget_metadata_list = tuple(self._widget_metadata_list)
        self._widget_self_list = tuple(self._widget_self_list)
    
    def logout(self, lvl: int = 0, text: str = '') -> None: consoleLogout(f'{__class__.__name__}@{self}', lvl, text)

    def rebuild(self) -> None:
        self._widget_self_list: list | tuple = []
        self._widget_metadata_list: list | tuple = []