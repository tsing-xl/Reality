from .interface import Interface
from .widgets import *
from .consolelogs import consoleLogout

class ExampleApp:
    def __init__(self):
        
        self.interface = Interface()

        self.button = Button(interface = self.interface, x = 50, y = 250, width = 200, height = 50, text = 'Jump to the next space!', command = self.onButtonClick)

        self.interface.runApplication()
    
    def onButtonClick(self) -> None:
        print('Button clicked! Recomposing interface...')
        self.interface.composer.recompose()
        self.interface.widget_handler.rebuild()
        
        # Change to cornflower blue (100, 149, 237)
        # Better way: 
        
        # self.button.updateElement('color', (100, 149, 237))
        self.button.updateElement('_text', 'Recomposed!')

        # Unrecommend way:
        # self.button.color = (100, 149, 237)

        self.button.recompose()

if __name__ == '__main__':
    app = ExampleApp()