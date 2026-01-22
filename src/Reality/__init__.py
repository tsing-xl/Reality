from .interface import Interface
from .widgetcomposer import WidgetComposer
from .widgethandler import WidgetHandler
from .widgets import Button
from .consolelogs import consoleLogout
from .background import Background
from .soundhandler import SoundHandler

__version__ = '1.00.00-unstable'
__version_v2__ = (1, 00, 00, 'unstable')

consoleLogout(log_String = f'Reality UI built on pyglet. Version {__version__}.')

if __version_v2__[-1] == 'unstable': consoleLogout(level = 1, log_String = 'You are now using a unstable version, the unstable version may contains some experiment features or unreported bugs.')

__all__ = (
    'Interface',
    'WidgetComposer',
    'WidgetHandler',
    'Button',
    'Label',
    'Cover', 
    'Background',
    'consoleLogout',
    '__version__',
    '__version_v2__',
    'SoundHandler',
)