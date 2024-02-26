from pathlib import Path
import json

MAIN_FOLDER_PATH = Path.home() / "Documents" / "Gestion des notes"
SETTINGS_FILE_PATH = MAIN_FOLDER_PATH / "settings.json"

def load_settings():
    if SETTINGS_FILE_PATH.exists():
        with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {"current_year": "None", "last_trimester": "None"}

def update_settings(new_year):
    settings = {"current_year": new_year, "last_trimester": "None"}
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f)