from .consolelogs import consoleLogout

__version__ = '1.0.0'
__version_v2__ = (1, 0, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Metadata module version {__version__}.')

class Metadata:
    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
        ):

        self._x, self._y = x, y
        self._w, self._h = width, height

        self.metadata = (x, y, width, height)
        self.metadata_v2 = (x, y, x + width, y + height)
    
    def updateMetadata(self, x: int, y: int, width: int, height: int) -> None:
        self._x, self._y = x, y
        self._w, self._h = width, height

        self.metadata = (x, y, width, height)
        self.metadata_v2 = (x, y, x + width, y + height)