from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QLabel, QSizePolicy
from PySide6.QtCore import Qt
import re

from pathlib import Path

from matplotlib import layout_engine

import Widgets.Styles.pop_up as style

import Modules.settings_module as settings_modules

class AddStudentDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(style.dialog_minimum_width, style.dialog_minimum_height)
        self.setWindowTitle("Ajouter un élève")

        settings = settings_modules.load_settings()
        
        current_class_path = Path(settings['current_class_path'])

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_lbl_class_layout = QVBoxLayout()

        wrapper_btn_layout = QHBoxLayout()
        wrapper_btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_lbl_tips_layout= QVBoxLayout()

        self.lbl_class = QLabel(f"La classe selectionner est {current_class_path.name}")
        self.lbl_class.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.qle_surname = QLineEdit(self)
        self.qle_surname.setPlaceholderText("Entrer le nom de l'élève")
        self.input_text_surname = ""

        self.qle_firstname = QLineEdit(self)
        self.qle_firstname.setPlaceholderText("Entrer le prénom de l'élève")
        self.input_text_firstname = ""

        self.btnOk = QPushButton("Valider", self)
        self.btnOk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btnOk.clicked.connect(self.validateInput)

        self.btnCancel = QPushButton("Annuler", self)
        self.btnCancel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btnCancel.clicked.connect(self.reject) # Ferme la dialogue avec un résultat "reject"

        self.lbl_tips = QLabel("Vous ne pouvez pas mettre de caractères spéciaux ni d'espaces")

 
        wrapper_lbl_class_layout.addWidget(self.lbl_class)
        wrapper_lbl_class_layout.setContentsMargins(style.lbl_class_margin_left, style.lbl_class_margin_top, style.lbl_class_margin_right, style.lbl_class_margin_bottom)

        wrapper_btn_layout.addWidget(self.btnOk)
        wrapper_btn_layout.addWidget(self.btnCancel)

        wrapper_lbl_tips_layout.addWidget(self.lbl_tips)
        wrapper_lbl_tips_layout.setContentsMargins(style.lbl_tips_margin_left, style.lbl_tips_margin_top, style.lbl_tips_margin_right, style.lbl_tips_margin_bottom)
        
        main_layout.addLayout(wrapper_lbl_class_layout)
        main_layout.addWidget(self.qle_surname)
        main_layout.addWidget(self.qle_firstname)
        main_layout.addLayout(wrapper_btn_layout)
        main_layout.addLayout(wrapper_lbl_tips_layout)


        self.setLayout(main_layout)


    def validateInput(self):
        input_surname = self.qle_surname.text()
        input_firstname = self.qle_firstname.text()
        
        if re.match("^[a-zA-Z0-9]+$", input_surname) and re.match("^[a-zA-Z0-9]+$", input_firstname):
            self.input_surname = input_surname
            self.input_firstname = input_firstname
            self.accept() # Ferme la dialogue avec un résultat "accept"
        else:
            QMessageBox.warning(self, "Erreur", "L'entrée ne doit contenir ni espaces ni caractères spéciaux.")       

