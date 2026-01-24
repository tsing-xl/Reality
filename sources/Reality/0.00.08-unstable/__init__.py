from .interface import Interface
# [Outdated features] from .widgetcomposer import WidgetComposer
from .composer.widgetcomposer import WidgetComposer
# [Outdated features] from .widgethandler import WidgetHandler
from .handler.widgethandler import WidgetHandler
from .widgets import *
from .consolelogs import consoleLogout
from .background import Background

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
    'CheckBox',
    'Background',
    'consoleLogout',
    '__version__',
    '__version_v2__',
)