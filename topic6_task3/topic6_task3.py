import sys
from pathlib import Path
from colorama import Fore, Style
from colorama import init

init()  

def iterate_folder(path, prefix=""):
    try:
        files = list(path.iterdir())
    except PermissionError:
        print(prefix + "├── " + Fore.RED + "Permission Denied" + Style.RESET_ALL)
        return
    except FileNotFoundError:
        print(Fore.RED + f"Error: Path '{path}' not found." + Style.RESET_ALL)
        return

    for index, el in enumerate(files):
        is_last_element = index == len(files) - 1
        connector = '└── ' if is_last_element else '├── '

        if el.is_dir():
            display_name = Fore.BLUE + el.name + "/" + Style.RESET_ALL
            print(prefix + connector + display_name)
            
            extension = '    ' if is_last_element else '│   '
            iterate_folder(el, prefix + extension)
        else:
            display_name = Fore.GREEN + el.name + Style.RESET_ALL
            print(prefix + connector + display_name)


if len(sys.argv) > 1:
    start_path = Path(sys.argv[1])
else:
    start_path = Path(r"topic6_task3/picture") 


print(Fore.CYAN + f"Scanning: {start_path}" + Style.RESET_ALL)
iterate_folder(start_path)
    
