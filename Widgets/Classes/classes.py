from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class ClassesWidget(QWidget):
     def __init__(self):
        super().__init__()
        self.setMaximumHeight(50)
        layout = QHBoxLayout()

        self.setLayout(layout)