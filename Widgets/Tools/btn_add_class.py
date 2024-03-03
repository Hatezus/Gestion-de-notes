from PySide6.QtWidgets import QPushButton, QMessageBox
from pathlib import Path

import Modules.check_module as check_module
import Modules.settings_module as settings_module
import Widgets.Pop_Up.pop_up_add_class as pop_up_add_class


class AddClassBtn(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.clicked.connect(self.on_click)

    def on_click(self):
        if check_module.check_active_year():
            dialog = pop_up_add_class.AddClassDialog()
            if dialog.exec_():
                user_input = dialog.input_text

                settings = settings_module.load_settings()

                path_to_folder = Path(settings['current_year_path'])
                path_to_folder = path_to_folder / user_input
                
                if path_to_folder.exists():
                    QMessageBox.critical(self, "Error", f"Il y a déjà une classe avec ce nom")
                else: 
                    if "classes" not in settings:
                        settings["classes"] = [user_input]
                        settings_module.save_settings(settings)
                    else: 
                        settings["classes"].append(user_input)
                        settings_module.save_settings(settings)
                    
                    path_to_folder.mkdir()
                    path_to_folder_student = path_to_folder / "Students"
                    path_to_folder_student.mkdir()
                    path_to_folder_t1 = path_to_folder / "1er Trimestre"
                    path_to_folder_t1.mkdir()
                    path_to_folder_t2 = path_to_folder / "2ème Trimestre"
                    path_to_folder_t2.mkdir()
                    path_to_folder_t3 = path_to_folder / "3ème Trimestre"
                    path_to_folder_t3.mkdir()

        
        else:
            QMessageBox.critical(self, "Error", f"Il n'y à pas d'année en cours")