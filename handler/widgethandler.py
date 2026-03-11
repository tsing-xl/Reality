from typing import Callable
from ..log4r import logout
# from threading import Thread

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

    def logout(self, lvl: int = 0, text: str = '') -> None: logout(f'{__class__.__name__}@{self}', lvl, text)