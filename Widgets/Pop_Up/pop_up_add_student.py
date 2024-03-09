from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QLabel, QSizePolicy
from PySide6.QtCore import Qt
import re

import Widgets.Styles.pop_up as style

class AddStudentDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(style.dialog_minimum_width, style.dialog_minimum_height)
        self.setWindowTitle("Ajouter une classe")

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_btn_layout = QHBoxLayout()
        wrapper_btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_lbl_layout= QVBoxLayout()

        self.qle = QLineEdit(self)
        self.qle.setPlaceholderText("Entrez une classe")
        self.input_text = ""
        
        self.btnOk = QPushButton("Valider", self)
        self.btnOk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btnOk.clicked.connect(self.validateInput)

        self.btnCancel = QPushButton("Annuler", self)
        self.btnCancel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btnCancel.clicked.connect(self.reject) # Ferme la dialogue avec un résultat "reject"

        self.lbl = QLabel("""Vous ne pouvez pas mettre de caractères spéciaux ni d'espaces
Vous ne pourrez pas avoir deux classes avec l'exact même nom
Si vous avez deux classes de même niveaux, vous pouvez faire par exemple CM1_1 et CM1_2
""")

        wrapper_lbl_layout.addWidget(self.lbl)
        wrapper_lbl_layout.setContentsMargins(style.lbl_margin_left, style.lbl_margin_top, style.lbl_margin_right, style.lbl_margin_bottom)

        wrapper_btn_layout.addWidget(self.btnOk)
        wrapper_btn_layout.addWidget(self.btnCancel)

        main_layout.addWidget(self.qle)
        main_layout.addLayout(wrapper_btn_layout)
        main_layout.addLayout(wrapper_lbl_layout)
        
        
        self.setLayout(main_layout)
       

    def validateInput(self):
        inputText = self.qle.text()
        if re.match("^[a-zA-Z0-9_]+$", inputText):
            self.input_text = inputText
            self.accept() # Ferme la dialogue avec un résultat "accept"
        else:
            QMessageBox.warning(self, "Erreur", "L'entrée ne doit contenir ni espaces ni caractères spéciaux.")       

