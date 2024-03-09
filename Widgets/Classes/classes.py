from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QButtonGroup
from functools import partial
from pathlib import Path

import Modules.settings_module as settings_module

class ClassesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(50)
        self.classes_btn_group = QButtonGroup()
        self.main_layout = QHBoxLayout()  # Créez le layout principal ici et réutilisez-le
        self.setLayout(self.main_layout)  # Définissez le layout du widget dès le début
        self.initUI()

    def initUI(self):
        self.clearLayout()  # Efface le contenu du layout existant
        settings = settings_module.load_settings()

        if "classes" in settings and settings["classes"]:
            for class_name in settings["classes"]:
                button = QPushButton(class_name)
                button.setCheckable(True)
                button.clicked.connect(partial(self.buttonClicked, class_name))
                self.classes_btn_group.addButton(button)
                self.main_layout.addWidget(button)  # Ajoutez le bouton au layout principal

            self.classes_btn_group.setExclusive(True)

    def refresh(self):
        self.initUI()  # Rafraîchit l'interface utilisateur

    def clearLayout(self):
        # Supprime tous les widgets du layout actuel
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def buttonClicked(self, class_name):
        settings = settings_module.load_settings()
        current_class_path = Path(settings['current_year_path'])
        current_class_path = current_class_path / class_name
        print(current_class_path)
        settings_module.update_settings('current_class_path', current_class_path.as_posix())