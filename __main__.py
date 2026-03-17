from .interface import Interface
from .widgets import widget, widget_texture

# Reality Description:
# Reality is a simple UI framework built on pyglet.
# It provides basic UI components and an easy-to-use interface for building applications.

class ExampleApp:
    def __init__(self):
        self.interface = Interface()

        self.blur_bg = widget_texture.ImageTexture(self.interface, 0, 0, 200, 50)
        self.cv0 = widget.BluredCover(self.interface, 0, 0, 200, 50, self.blur_bg)

        self.button_1 = widget.Button(self.interface, 0, 0, 200, 50, 'Hello, Reality!')
        
        self.interface.runApplication()

if __name__ == '__main__':
    app = ExampleApp()