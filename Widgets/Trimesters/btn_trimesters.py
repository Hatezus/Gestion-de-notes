from PySide6.QtWidgets import QPushButton, QMessageBox

import Modules.settings_module as settings_module


class TrimestersBtn(QPushButton):
    def __init__(self, text, btn_id):
        super().__init__(text)

        self.btn_id = btn_id 
        self.setCheckable(True)
        self.clicked.connect(self.on_click) 


    def on_click(self):
        if self.btn_id == 1:
            settings_module.update_settings("trimester", 1) 
        elif self.btn_id == 2:
            settings_module.update_settings("trimester", 2) 
        elif self.btn_id == 3:
            settings_module.update_settings("trimester", 3) 

