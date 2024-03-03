from pathlib import Path
import json

MAIN_FOLDER_PATH = Path.home() / "Documents" / "Gestion des notes"
SETTINGS_FILE_PATH = MAIN_FOLDER_PATH / "settings.json"


def first_start():
    if MAIN_FOLDER_PATH.exists() == False:
        MAIN_FOLDER_PATH.mkdir(parents=True)
        SETTINGS_FILE_PATH.touch()
        with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
            settings = {
                "current_year_path" : "None", 
                "trimester" : 0, 
                "main_folder_path": MAIN_FOLDER_PATH.as_posix(), 
                "settings_path": SETTINGS_FILE_PATH.as_posix()}
            json.dump(settings, f, ensure_ascii=False, indent=4)


def load_settings() -> dict:
    with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_settings(settings):
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)


def update_settings(key, new_value):
    settings = load_settings()
    settings[key] = new_value
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)