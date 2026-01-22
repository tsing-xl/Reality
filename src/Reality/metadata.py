from .consolelogs import consoleLogout

__version__ = '1.0.0'
__version_v2__ = (1, 0, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Metadata module version {__version__}.')

class Metadata_v0:
    def __init__(self, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h

        self._tupl = (x, y, w, h)
    
    def returnTuple(self) -> tuple: return self._tupl

class Metadata_v2:
    def __init__(self, x, y, w, h):
        self._x, self._y = x, y
        self._xw, self._yh = x + w, y + h

        self._tupl = (x, y, self._xw, self._yh)
    
    def returnTuple(self) -> tuple: return self._tupl