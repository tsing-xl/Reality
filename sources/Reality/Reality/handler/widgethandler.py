from typing import Callable
from ..consolelogs import consoleLogout
# from threading import Thread

__version__ = '1.1.0'
__version_v2__ = (1, 1, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Widgethandler module version {__version__}.')

class WidgetHandler:
    def __init__(self):
        self.recompose()
    
    def registerWidget(self, widget_self) -> None:
        self.widget_self_list.append(widget_self)
    
    def motionHandler(self, x, y, *kw) -> None:
        for __index in self.widget_self_list: __index.onMouseMotion(x, y)
    
    def clickHandler(self, x, y, *kw) -> None:
        for __index in self.widget_self_list: __index.onMouseClick(x, y)
    
    def frozen(self) -> None: self.widget_self_list = tuple(self.widget_self_list)

    def recompose(self) -> None: self.widget_self_list: list | tuple = []

    def logout(self, lvl: int = 0, text: str = '') -> None: consoleLogout(f'{__class__.__name__}@{self}', lvl, text)