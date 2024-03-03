from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import QRegularExpression 
from PySide6.QtGui import QRegularExpressionValidator

import Widgets.Styles.no_active_year as style

class YearLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QRegularExpressionValidator(QRegularExpression(r'^\d{4}$')))

        self.setFixedSize(style.qle_width, style.qle_height)