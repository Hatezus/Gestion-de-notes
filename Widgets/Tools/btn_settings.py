from PySide6.QtWidgets import QPushButton, QMessageBox
from PySide6.QtCore import Signal

import Modules.check_module as check_module


class Settingsbtn(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.clicked.connect(self.on_click)

    def on_click(self):
        if check_module.check_active_year():
            pass
        else:
            QMessageBox.critical(self, "Error", f"Il n'y à pas d'année en cours")