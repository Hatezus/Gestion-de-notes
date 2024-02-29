from PySide6.QtWidgets import QWidget, QHBoxLayout

import Widgets.No_Active_Year.lbl_msg as lbl_msg
import Widgets.No_Active_Year.qle_year as qle_year
import Widgets.No_Active_Year.btn_validation as btn_validation




class NoActiveYearWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        self.lbl_msg = lbl_msg.MessageLabel("Il n'y a pas d'année en cours")
        self.qle_year_1 = qle_year.YearLineEdit()
        self.qle_year_2 = qle_year.YearLineEdit()
        self.btn_validation = btn_validation.ValidationBtn("Valider",self.qle_year_1, self.qle_year_2)

        self.btn_validation.operation_successful.connect(self.delete_widget)

        layout.addWidget(self.lbl_msg)
        layout.addWidget(self.qle_year_1)
        layout.addWidget(self.qle_year_2)
        layout.addWidget(self.btn_validation)
        
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

 