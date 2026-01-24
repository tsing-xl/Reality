from .interface import Interface
from .widgets import *
from .consolelogs import consoleLogout

# Reality Description:
# Reality is a simple UI framework built on pyglet.
# It provides basic UI components and an easy-to-use interface for building applications.

class ExampleApp:
    def __init__(self):
        
        self.interface = Interface()

        self.button = Button(interface = self.interface, x = 50, y = 250, width = 200, height = 50, text = 'Jump to the next space!', command = self.onButtonClick)

        self.interface.runApplication()
    
    def onButtonClick(self) -> None:
        self.interface.recompose()
        
        # Change to cornflower blue (100, 149, 237)
        # Better way: 
        
        # self.button.updateElement('color', (100, 149, 237))
        self.button.updateText('Jumped!')

        self.checkbox = CheckBox(interface = self.interface, x = 50, y = 180, text = 'Enable feature X', is_checked = True)
        self.checkbox = CheckBox(interface = self.interface, x = 50, y = 150, text = 'Enable feature Y', is_checked = False)
        self.checkbox = CheckBox(interface = self.interface, x = 50, y = 120, text = 'Enable feature Z', is_checked = False)

        self.button.recompose()

if __name__ == '__main__':
    app = ExampleApp()