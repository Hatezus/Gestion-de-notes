from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QButtonGroup, QMessageBox, QLineEdit
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

def load_settings():
    if SETTINGS_FILE_PATH.exists():
        with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {"current_year": "None", "last_trimester": "None"}

def update_settings(new_year):
    settings = {"current_year": new_year, "last_trimester": "None"}
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de notes")

        self.settings = load_settings()
        
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

        if self.settings["current_year"] == "None":
            self.init_first_time_display(main_layout)


        # Adding tools_widget and classes_widget to the main layout
        main_layout.addWidget(tools_widget)
        main_layout.addWidget(classes_widget)
        main_layout.addWidget(trimester_widget)
        main_layout.addWidget(display_widget)

        # Set the main layout to the main window
        self.setLayout(main_layout)


    def init_first_time_display(self, layout):
        self.first_time_display = QWidget()
        first_time_layout = QHBoxLayout(self.first_time_display)
        
        label = QLabel("Bienvenue! Veuillez entrer l'année courante:")
        self.year_input = QLineEdit()  # Input for year
        add_year_btn = QPushButton("Ajouter l'année")

        # Connect the button's click signal to the slot that handles year addition
        add_year_btn.clicked.connect(self.add_year)

        first_time_layout.addWidget(label)
        first_time_layout.addWidget(self.year_input)
        first_time_layout.addWidget(add_year_btn)

        layout.addWidget(self.first_time_display)

    def add_year(self):
        new_year = self.year_input.text().strip()
        if new_year:
            update_settings(new_year)
            self.settings["current_year"] = new_year  # Update settings in memory
            self.first_time_display.setVisible(False)  # Hide the widget
            QMessageBox.information(self, "Mise à jour", "L'année a été ajoutée avec succès.")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une année valide.")






























































if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
