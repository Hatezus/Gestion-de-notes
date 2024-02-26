from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QButtonGroup
from pathlib import Path
import json


MAIN_FOLDER_PATH = Path.home() / "Documents" / "Gestion des notes"
SETTINGS_FILE_PATH = MAIN_FOLDER_PATH / "settings.json"

if MAIN_FOLDER_PATH.exists() == False:
    MAIN_FOLDER_PATH.mkdir(parents=True)
    SETTINGS_FILE_PATH.touch()
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
        settings = {"current_year" : "None", "last_trimester" : "None"}
        json.dump(settings, f)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de notes")

        
        # The main layout for the main_widget
        main_layout = QVBoxLayout()

        # Setup for tools_widget and its layout
        tools_widget = QWidget()
        tools_layout = QHBoxLayout()
        tools_widget.setMaximumHeight(50)
        tools_widget.setLayout(tools_layout)  # Apply the layout to tools_widget

        # Adding buttons to tools_layout
        tools_layout.addWidget(QPushButton("Ajouter une classe"))
        tools_layout.addWidget(QPushButton("Ajouter un élève"))
        tools_layout.addWidget(QPushButton("Ajouter une note"))
        tools_layout.addWidget(QPushButton("Générer les bulletins"))
        tools_layout.addWidget(QPushButton("Retirer un élève"))
        tools_layout.addWidget(QPushButton("Paramètres"))

        # Setup for classes_widget and its layout (though not populated in your snippet)
        classes_widget = QWidget()
        classes_layout = QHBoxLayout()
        classes_widget.setMaximumHeight(50)
        classes_widget.setLayout(classes_layout)  # Apply the layout to classes_widget

        trimester_widget = QWidget()
        trimester_layout = QHBoxLayout()
        trimester_widget.setMaximumHeight(50)
        trimester_widget.setLayout(trimester_layout)

        # Create the trimester buttons and make them checkable
        btn_first_trimester = QPushButton("Premier Trimestre")
        btn_first_trimester.setCheckable(True)
        btn_second_trimester = QPushButton("Deuxième Trimestre")
        btn_second_trimester.setCheckable(True)
        btn_third_trimester = QPushButton("Troisième Trimestre")
        btn_third_trimester.setCheckable(True)

        # Add buttons to the trimester_layout
        trimester_layout.addWidget(btn_first_trimester)
        trimester_layout.addWidget(btn_second_trimester)
        trimester_layout.addWidget(btn_third_trimester)

        # Use QButtonGroup to manage the toggle state
        self.trimester_button_group = QButtonGroup()
        self.trimester_button_group.addButton(btn_first_trimester, 1)
        self.trimester_button_group.addButton(btn_second_trimester, 2)
        self.trimester_button_group.addButton(btn_third_trimester, 3)
        self.trimester_button_group.setExclusive(True)  # Ensure only one button can be checked

        trimester_layout.addWidget(btn_first_trimester)
        trimester_layout.addWidget(btn_second_trimester)
        trimester_layout.addWidget(btn_third_trimester)


        display_widget = QWidget()
        display_layout = QVBoxLayout()
        display_widget.setMinimumHeight(500)
        display_widget.setLayout(display_layout)



        # Adding tools_widget and classes_widget to the main layout
        main_layout.addWidget(tools_widget)
        main_layout.addWidget(classes_widget)
        main_layout.addWidget(trimester_widget)
        main_layout.addWidget(display_widget)

        # Set the main layout to the main window
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
