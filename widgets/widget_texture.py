from ..utils import createFolder, ScreenCapture
from ..interface import Interface
from PIL import Image, ImageFilter
from uuid import uuid4
from .t4ppc import transfer

createFolder('./oxcache')

class ImageTexture:
    def __init__(
            self, 
            interface: Interface, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            strength: int = 20, 
        ) -> None:

        '''Create a texture for Cover widgets.'''
        self.interface = interface
        self.interface_background_filename = interface.background.filename

        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height

        self.strength = strength

        # Step 1: Crop the image.
        original_image = Image.open(self.interface_background_filename)
        original_image = original_image.crop(
            transfer(
                self.x, 
                self.y, 
                self.width, 
                self.height, 
                self.interface.width, 
                self.interface.height, 
            )
        )

        # Step 2: Blur the image. (By Gaussian-blur)
        original_image = original_image.filter(ImageFilter.GaussianBlur(self.strength))

        # Step 3: Storage them into cache folder.
        self.filename = f'./oxcache/{uuid4()}.png'
        original_image.save(self.filename)