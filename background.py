from pyglet import image, sprite
from pathlib import Path
# from .log4r import logout

class Background:
    def __init__(self, images: str | None = None) -> None:
        # Load background image
        package_dir = Path(__file__).parent.resolve()

        # Load default background if no image provided
        if images is None: self._img = image.load(filename = package_dir / 'background.png')
        else: self._img = image.load(filename = images)

        # TODO: Push it into background batch later
        self._sprite = sprite.Sprite(self._img, 0 ,0)
    
    def drawBackground(self) -> None: self._sprite.draw()