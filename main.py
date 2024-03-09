import Modules.settings_module as settings_module
settings_module.first_start()

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from Widgets.Tools.tools import ToolsWidget
from Widgets.Classes.classes import ClassesWidget
from Widgets.Trimesters.trimesters import TrimestersWidget
from Widgets.Display.display import DisplayWidget


import importlib
importlib.reload(settings_module)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion de notes")
        
        main_layout = QVBoxLayout()

        self.tools_widget = ToolsWidget()
        self.classes_widget = ClassesWidget()
        self.trimesters_widget = TrimestersWidget()
        self.display_widget = DisplayWidget()   
        

        main_layout.addWidget(self.tools_widget)
        main_layout.addWidget(self.classes_widget)
        main_layout.addWidget(self.trimesters_widget)
        main_layout.addWidget(self.display_widget)

        self.tools_widget.class_added_signal.connect(self.classes_widget.refresh)

        self.setLayout(main_layout)
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
