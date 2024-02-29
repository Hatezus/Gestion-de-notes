from PySide6.QtWidgets import QPushButton, QMessageBox

import Modules.path_dir as path_dir


MAIN_FOLDER_PATH = path_dir.MAIN_FOLDER_PATH

class ValidationBtn(QPushButton):
    def __init__(self, text, line_edit1, line_edit2):
        super().__init__(text)
        self.line_edit1 = line_edit1
        self.line_edit2 = line_edit2
        self.clicked.connect(self.on_click)

    def on_click(self):
        year1 = self.line_edit1.text()
        year2 = self.line_edit2.text()
        if year1.isdigit() and year2.isdigit() and len(year1) == 4 and len(year2) == 4:
            folder_name = f"{year1}-{year2}"
            try:
                year_folder = MAIN_FOLDER_PATH / folder_name
                year_folder.mkdir()
                QMessageBox.information(self, "Success", "Folder created successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not create folder: {e}")
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter 4-digit years in both fields.")