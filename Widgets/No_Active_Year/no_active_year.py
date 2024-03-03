from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

import Widgets.No_Active_Year.lbl_msg as lbl_msg
import Widgets.No_Active_Year.qle_year as qle_year
import Widgets.No_Active_Year.btn_validation as btn_validation




class NoActiveYearWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        wrapper_lbl_1_layout = QHBoxLayout()
        wrapper_lbl_1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_lbl_2_layout = QHBoxLayout()
        wrapper_lbl_2_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_qle_layout = QHBoxLayout()
        wrapper_qle_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        wrapper_btn_layout = QHBoxLayout()
        wrapper_btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.lbl_msg_1 = lbl_msg.MessageLabel("Il n'y a pas d'année en cours")
        self.lbl_msg_2 = lbl_msg.MessageLabel("Veuillez entrer une année")
        self.qle_year_1 = qle_year.YearLineEdit()
        self.qle_year_2 = qle_year.YearLineEdit()
        self.btn_validation = btn_validation.ValidationBtn("Valider",self.qle_year_1, self.qle_year_2)

        self.btn_validation.operation_successful.connect(self.delete_widget)

        wrapper_lbl_1_layout.addWidget(self.lbl_msg_1)
        wrapper_lbl_2_layout.addWidget(self.lbl_msg_2)
        wrapper_qle_layout.addWidget(self.qle_year_1)
        wrapper_qle_layout.addWidget(self.qle_year_2)
        wrapper_btn_layout.addWidget(self.btn_validation)
        
        main_layout.addLayout(wrapper_lbl_1_layout)
        main_layout.addLayout(wrapper_lbl_2_layout)
        main_layout.addLayout(wrapper_qle_layout)
        main_layout.addLayout(wrapper_btn_layout)
        
        
        
    def delete_widget(self):
    # Remove the widget from its layout first
        if self.layout() is not None:
            while self.layout().count():
                item = self.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.layout().removeItem(item)

        self.deleteLater() 

 