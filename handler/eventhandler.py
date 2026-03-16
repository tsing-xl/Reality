from typing import Callable
from ..log4r import logout
from pyglet import clock

__version__ = '1.0.0'
__version_v2__ = (1, 0, 0, 'unstable')

logout(f'{__name__}@<PythonModule>', 0, f'Eventhandler module version {__version__}.')

class Event:
    def __init__(self, function_name: Callable) -> None:
        self._function = function_name
    
    def executeFunction(self) -> any:
        return self._function()
    
    def rewriteFunction(self, new_function: Callable) -> None:
        self._function = new_function

class ScheduleEvent:
    def __init__(self, schedule_function: Callable, execute_once: bool = False, duration: int | float = 1.0) -> None:
        if execute_once: self._once = True