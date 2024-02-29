from PySide6.QtWidgets import QLabel

class CustomLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)