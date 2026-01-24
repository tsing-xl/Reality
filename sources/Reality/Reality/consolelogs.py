from colorama import init, Fore, Style
from os import name

__version__ = '1.0.0'
__version_v2__ = (1, 0, 0, 'stable')

if name == 'nt': init(True, wrap = True)
else: init(True)

log_lvl: tuple = (
    Fore.LIGHTBLUE_EX + 'Infomation', 
    Fore.LIGHTBLACK_EX + 'Suggestion', 
    Fore.YELLOW + 'Warning', 
    Fore.LIGHTRED_EX + 'Error', 
    Fore.RED + 'Fatal', 
    Fore.MAGENTA + 'Debug', 
)

def consoleLogout(
        from_location: str = 'Reality', 
        level: int = 0, 
        log_String: str = ''
    ) -> None: 
    
    print(f'{log_lvl[min(level, 5)]}: {Style.RESET_ALL}{log_String} {Fore.LIGHTBLACK_EX}(From {from_location})')

consoleLogout(f'{__name__}@<PythonModule>', 0, f'Consolelogs module version {__version__}.')