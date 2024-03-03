from PySide6.QtWidgets import QPushButton, QMessageBox
from PySide6.QtCore import Signal
from pathlib import Path

import Modules.settings_module as settings_module

import Widgets.Styles.no_active_year as style

settings = settings_module.load_settings()
MAIN_FOLDER_PATH = Path(settings["main_folder_path"])


class ValidationBtn(QPushButton):

    operation_successful = Signal()

    def __init__(self, text, line_edit1, line_edit2):
        super().__init__(text)
        self.line_edit1 = line_edit1
        self.line_edit2 = line_edit2
        self.clicked.connect(self.on_click)

        self.setFixedSize(style.btn_width, style.btn_height)

    def on_click(self):
        year1 = self.line_edit1.text()
        year2 = self.line_edit2.text()
        if year1.isdigit() and year2.isdigit() and len(year1) == 4 and len(year2) == 4:
            folder_name = f"{year1}-{year2}"
            try:
                year_folder = MAIN_FOLDER_PATH / folder_name
                year_folder.mkdir()
                QMessageBox.information(self, "Success", "L'année a été créer avec succès !")
                settings_module.update_settings("current_year_path", year_folder.as_posix())
                self.operation_successful.emit()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Le dossier n'as pas pus être créer: {e}")
        else:
            QMessageBox.warning(self, "Saisie incorrecte", "Veillez entrer une valeur à 4 chiffres.")