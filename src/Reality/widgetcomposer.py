from pyglet import graphics
from typing import Callable
from .consolelogs import consoleLogout

__version__ = '1.3.0'
__version_v2__ = (1, 3, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Widgetcomposer module version {__version__}.')

class WidgetComposer:
    def __init__(self, interface_self: any = None):
        
        # 用于与界面类进行交互。未使用的功能。
        self._interface = interface_self

        # 3 Layers of widget: (background) >> Cover layer (Private) >> Graphics layer >> Text layer >> Top widget layer
        # 背景层 >> 图形层 >> 文字层 >> 顶层
        self.recompose()
    
    def drawComposer(self) -> None:
        self.under_cover_batch.draw()
        self.graphics_batch.draw()
        self.text_batch.draw()
    
    def recompose(self) -> None:
        if hasattr(self, 'under_cover_batch'):
            del self.under_cover_batch
            del self.graphics_batch
            del self.text_batch

        self.under_cover_batch = graphics.Batch()
        self.graphics_batch = graphics.Batch()
        self.text_batch = graphics.Batch()

    def logout(self, lvl: int = 0, text: str = '') -> None: consoleLogout(f'{__class__.__name__}@{self}', lvl, text)