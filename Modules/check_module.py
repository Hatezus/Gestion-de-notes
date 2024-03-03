import Modules.settings_module as settings_module

from pathlib import Path


def check_active_year() -> bool:
    settings = settings_module.load_settings()
    current_year_path = settings.get("current_year_path", "None")
    
    if current_year_path != "None":
        return True 
    else:
        return False


def check_trimester() -> int:
    settings = settings_module.load_settings()
    current_trimester = settings.get("trimester", 0)
    return current_trimester


