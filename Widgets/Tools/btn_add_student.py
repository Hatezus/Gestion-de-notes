from PySide6.QtWidgets import QPushButton, QMessageBox
from pathlib import Path

import Modules.check_module as check_module
import Modules.settings_module as settings_module
import Widgets.Pop_Up.pop_up_add_student as pop_up_add_student


class AddStudentBtn(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.clicked.connect(self.on_click)

    def on_click(self):
        if check_module.check_active_year():
            dialog = pop_up_add_student.AddStudentDialog()
            if dialog.exec_():
                pass
        else:
            QMessageBox.critical(self, "Error", f"Il n'y à pas d'année en cours")