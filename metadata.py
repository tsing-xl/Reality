from .log4r import logout

class Metadata:
    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
        ):
        '''The metadata module is used to transfer widget's location infomation prettier.
        Readable code is more import than perfomance, especially for a little.'''

        self._x, self._y = x, y
        self._w, self._h = width, height

        self.metadata = (x, y, width, height)
        self.metadata_v2 = (x, y, x + width, y + height)
    
    def updateMetadata(self, x: int, y: int, width: int, height: int) -> None:
        self._x, self._y = x, y
        self._w, self._h = width, height

        self.metadata = (x, y, width, height)
        self.metadata_v2 = (x, y, x + width, y + height)