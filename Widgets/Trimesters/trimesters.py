from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QButtonGroup


import Widgets.Trimesters.btn_trimesters as btn_trimesters

class TrimestersWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(50)
        layout = QHBoxLayout()
        

        self.btn_trimesters_1 = btn_trimesters.TrimestersBtn("Premier Trimestre")
        self.btn_trimesters_1.setCheckable(True)
        self.btn_trimesters_2 = btn_trimesters.TrimestersBtn("Deuxième Trimestre")
        self.btn_trimesters_2.setCheckable(True)
        self.btn_trimesters_3 = btn_trimesters.TrimestersBtn("Troisème Trimestre")
        self.btn_trimesters_3.setCheckable(True)
        
 
         # Use QButtonGroup to manage the toggle state
        self.trimester_button_group = QButtonGroup()
        self.trimester_button_group.addButton(self.btn_trimesters_1, 1)
        self.trimester_button_group.addButton(self.btn_trimesters_2, 2)
        self.trimester_button_group.addButton(self.btn_trimesters_3, 3)
        self.trimester_button_group.setExclusive(True)  # Ensure only one button can be checked

        layout.addWidget(self.btn_trimesters_1)
        layout.addWidget(self.btn_trimesters_2)
        layout.addWidget(self.btn_trimesters_3)


        self.setLayout(layout)