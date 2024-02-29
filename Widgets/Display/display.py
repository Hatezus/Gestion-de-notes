from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

from Widgets.No_Active_Year.no_active_year import NoActiveYearWidget


class DisplayWidget(QWidget):
     def __init__(self):
         super().__init__()
        
         self.setMinimumHeight(500)
        
         layout = QVBoxLayout()
         
         self.no_active_year_widget = NoActiveYearWidget()

         layout.addWidget(self.no_active_year_widget)
         
         self.setLayout(layout)