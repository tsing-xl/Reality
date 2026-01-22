from pyglet import image, sprite
from pathlib import Path
from .consolelogs import consoleLogout

__version__ = '1.0.0'
__version_v2__ = (1, 0, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Background module version {__version__}.')

class Background:
    def __init__(self, images: str | None = None) -> None:
        package_dir = Path(__file__).parent.resolve()
        if images is None: self._img = image.load(filename = package_dir / 'background.png')
        else: self._img = image.load(filename = images)

        self._sprite = sprite.Sprite(self._img, 0 ,0)
    
    def drawBackground(self) -> None: self._sprite.draw()