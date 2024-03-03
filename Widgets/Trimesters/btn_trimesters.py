from PySide6.QtWidgets import QPushButton, QMessageBox
from PySide6.QtCore import Signal



class TrimestersBtn(QPushButton):
    def __init__(self, text):
        super().__init__(text)