from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QButtonGroup

class TrimestersWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(50)
        layout = QHBoxLayout()
        
        
        btn_first_trimester = QPushButton("Premier Trimestre")
        btn_first_trimester.setCheckable(True)
        btn_second_trimester = QPushButton("Deuxième Trimestre")
        btn_second_trimester.setCheckable(True)
        btn_third_trimester = QPushButton("Troisième Trimestre")
        btn_third_trimester.setCheckable(True)

        
        layout.addWidget(btn_first_trimester)
        layout.addWidget(btn_second_trimester)
        layout.addWidget(btn_third_trimester)

        # Use QButtonGroup to manage the toggle state
        self.trimester_button_group = QButtonGroup()
        self.trimester_button_group.addButton(btn_first_trimester, 1)
        self.trimester_button_group.addButton(btn_second_trimester, 2)
        self.trimester_button_group.addButton(btn_third_trimester, 3)
        self.trimester_button_group.setExclusive(True)  # Ensure only one button can be checked

        layout.addWidget(btn_first_trimester)
        layout.addWidget(btn_second_trimester)
        layout.addWidget(btn_third_trimester)


        self.setLayout(layout)