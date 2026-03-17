from pyglet import image, sprite
from pathlib import Path
# from .log4r import logout

class Background:
    def __init__(self, images: str | None = None) -> None:
        # Load background image
        package_dir = Path(__file__).parent.resolve()

        # Load default background if no image provided
        self.filename = package_dir / 'background.png' if images is None else images
        self.img = image.load(filename = self.filename)

        # TODO: Push it into background batch later
        self._sprite = sprite.Sprite(self.img, 0 ,0)
    
    def drawBackground(self) -> None: self._sprite.draw()