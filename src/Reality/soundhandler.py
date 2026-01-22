from pyglet import media
from .consolelogs import consoleLogout

__version__ = '1.0.0'
__version_v2__ = (1, 0, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Soundhandler module version {__version__}.')

class SoundHandler:
    def __init__(self):
        '''A simple sound handler for Reality UI.'''

        self._player = media.Player()
        self._sound_list: list = []
    
    def loadSound(self, file_path: str) -> None:
        '''Load a file from file_path.'''
        sound = media.load(file_path, streaming = False)
        self._sound_list.append(sound)
    
    def nextSound(self) -> None:
        self._player.pause()
        self._player.next_source()
    
    def stopSound(self) -> None:
        '''Stop the currently playing sound.'''
        self._player.pause()
    
    def playSound(self, index: int = 0) -> None:
        '''Play the sound at the given index in the sound list.'''
        if self._player.is_playing: return
        self._player.play()