from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class ToolsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(50)
        layout = QHBoxLayout()

        # Adding buttons to layout
        layout.addWidget(QPushButton("Ajouter une classe"))
        layout.addWidget(QPushButton("Ajouter un élève"))
        layout.addWidget(QPushButton("Ajouter une note"))
        layout.addWidget(QPushButton("Générer les bulletins"))
        layout.addWidget(QPushButton("Retirer un élève"))
        layout.addWidget(QPushButton("Paramètres"))

        self.setLayout(layout)
