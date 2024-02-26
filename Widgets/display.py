from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class DisplayWidget(QWidget):
     def __init__(self):
        super().__init__()
        self.setMinimumHeight(500)
        layout = QVBoxLayout()

        self.setLayout(layout)