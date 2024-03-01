from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

from Widgets.No_Active_Year.no_active_year import NoActiveYearWidget
from Modules.settings_module import load_settings

class DisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setMinimumHeight(500)
        
        layout = QVBoxLayout()
         
        self.settings = load_settings()

        if self.settings["current_year"] == "None":

            self.no_active_year_widget = NoActiveYearWidget()

            layout.addWidget(self.no_active_year_widget)
            
        self.setLayout(layout)