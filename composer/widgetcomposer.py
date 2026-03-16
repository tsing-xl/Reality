from pyglet import graphics
from typing import Callable
from ..log4r import logout

class WidgetComposer:
    def __init__(
            self, interface: any = None) -> None:
        '''Compose the widgets easily.'''

        # Outdated features
        # self._interface = interface_self
        # self.interface = interface

        self.recompose()
    
    def draw(self) -> None:

        # Batch order: under-cover (bottom) -> graphics-batch -> text-batch
        self.under_cover_batch.draw()
        self.graphics_batch.draw()
        self.text_batch.draw()
    
    def recompose(self) -> None:
        self.logout(0, 'Recomposing WidgetComposer...')
        
        # Remove the old batch if possible.
        if hasattr(self, 'under_cover_batch'):
            del self.under_cover_batch
            del self.graphics_batch
            del self.text_batch

        # Add new graphics batch. (Possibly ~= reflush?)
        self.under_cover_batch = graphics.Batch()
        self.graphics_batch = graphics.Batch()
        self.text_batch = graphics.Batch()
        # TODO: Better recollection method.

        # self.logout(0, f'[New] self.under_cover_batch={self.under_cover_batch}')

    def logout(self, lvl: int = 0, text: str = '') -> None: logout(f'{__class__.__name__}@{self}', lvl, text)