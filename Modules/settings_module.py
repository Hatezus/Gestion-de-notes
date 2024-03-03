import Modules.path_dir as path_dir
import json

MAIN_FOLDER_PATH = path_dir.MAIN_FOLDER_PATH
SETTINGS_FILE_PATH = path_dir.SETTINGS_FILE_PATH


def first_start():
    if MAIN_FOLDER_PATH.exists() == False:
        MAIN_FOLDER_PATH.mkdir(parents=True)
        SETTINGS_FILE_PATH.touch()
        with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
            settings = {"current_year" : "None", "trimester" : "None"}
            json.dump(settings, f)


def load_settings():
    if SETTINGS_FILE_PATH.exists():
        with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return 

def update_settings(key, new_value):
    if SETTINGS_FILE_PATH.exists():
        with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as f:
            settings = {key: new_value}
        with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(settings, f)