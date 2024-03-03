import Modules.path_dir as path_dir
import Modules.settings_module as settings_module

MAIN_FOLDER_PATH = path_dir.MAIN_FOLDER_PATH
SETTINGS_FILE_PATH = path_dir.SETTINGS_FILE_PATH



def check_active_year() -> bool:
    settings = settings_module.load_settings()
    current_year = settings.get("current_year", "None")
    
    if current_year == "None":
        return False 
    else:
        return True


def check_trimester() -> int:
    settings = settings_module.load_settings()
    current_trimester = settings.get("trimester", 0)
    return current_trimester