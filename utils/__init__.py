from ..log4r import logout
from os import mkdir, path
from uuid import uuid4

# Try if mss contains
try: from mss import mss, tools
except: logout('Reality.utils', 2, 'Missing module mss. Screen capture, and gaussian-blur-background will not enabled.')


def createFolder(folder_name: str) -> bool:
    '''Creates a folder, if folder exists, then ignore.'''
    if path.exists(folder_name): return False

    mkdir(folder_name)
    return True

class ScreenCapture:
    def __init__(self):
        '''Capture screen with mss.'''
        
        self.sct = mss()
        
        self.monitor = self.sct.monitors[0]

        # Creates a folder to strage cached screen capture.
        createFolder('./screen-capture-cache')
    
    def captureOnce(self) -> str:
        img = self.sct.grab(self.monitor)
        tools.to_png(img.rgb, img.size, output=f"./screen-capture-cache/{uuid4()}.png")
    
    def quit(self) -> None: self.sct.close()