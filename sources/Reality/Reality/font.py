from pyglet import font
from .consolelogs import consoleLogout

__version__ = '1.1'
__version_v2__ = (1, 1, 0, 'unstable')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Font module version {__version__}.')

def loadFontFrom(font_path: str | None = None, font_name: str | None = None) -> None:
    '''
    Load fonts from given path. Accepts both file path and file-like object.
    
    :param font_path: Font file path or file-like object
    :param name: Name of the font to load
    '''

    if font_path is None: raise ValueError('font_path cannot be None.')

    if isinstance(font_path, str):
        try: 
            font.add_file(font_path)
        except: 
            consoleLogout(f'{__name__}@loadFontFrom', 3, f'Failed to load font from path: {font_path}')
            return
        
        consoleLogout(f'{__name__}@loadFontFrom', 0, f'Font loaded from path: {font_path}')

        try:
            font.load(font_name)
        except:
            consoleLogout(f'{__name__}@loadFontFrom', 2, f'Failed to load font with name: {font_name}')
            return

        consoleLogout(f'{__name__}@loadFontFrom', 0, f'Font loaded with name: {font_name}')