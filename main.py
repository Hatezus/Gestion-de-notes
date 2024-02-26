from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from pathlib import Path
import json
import Modules.settings_module as settings_module
from Widgets.tools import ToolsWidget
from Widgets.classes import ClassesWidget
from Widgets.trimesters import TrimestersWidget
from Widgets.display import DisplayWidget




MAIN_FOLDER_PATH = Path.home() / "Documents" / "Gestion des notes"
SETTINGS_FILE_PATH = MAIN_FOLDER_PATH / "settings.json"

if MAIN_FOLDER_PATH.exists() == False:
    MAIN_FOLDER_PATH.mkdir(parents=True)
    SETTINGS_FILE_PATH.touch()
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
        settings = {"current_year" : "None", "last_trimester" : "None"}
        json.dump(settings, f)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de notes")

        self.settings = settings_module.load_settings()
        
        main_layout = QVBoxLayout()

        self.tools_widget = ToolsWidget()
        self.classes_widget = ClassesWidget()
        self.trimesters_widget = TrimestersWidget()
        self.display_widget = DisplayWidget()        

        main_layout.addWidget(self.tools_widget)
        main_layout.addWidget(self.classes_widget)
        main_layout.addWidget(self.trimesters_widget)
        main_layout.addWidget(self.display_widget)


        self.setLayout(main_layout)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
