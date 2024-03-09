from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

import Widgets.Tools.btn_add_class as btn_add_class
import Widgets.Tools.btn_add_student as btn_add_student 
import Widgets.Tools.btn_add_grade as btn_add_grade
import Widgets.Tools.btn_produce_reports as btn_produce_reports
import Widgets.Tools.btn_remove_student as btn_remove_student
import Widgets.Tools.btn_settings as btn_settings


class ToolsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(50)
        main_layout = QHBoxLayout()


        self.btn_add_class = btn_add_class.AddClassBtn("Ajouter une classe")
        self.btn_add_student = btn_add_student.AddStudentBtn("Ajouter un élève")
        self.btn_add_grade = btn_add_grade.AddGradeBtn("Ajouter une note")
        self.btn_produce_reports = btn_produce_reports.ProduceReportsBtn("Générer les bulletins")
        self.btn_remove_student = btn_remove_student.RemoveStudentBtn("Retirer un élève")
        self.btn_settings = btn_settings.Settingsbtn("Paramètres")
        

        main_layout.addWidget(self.btn_add_class)
        main_layout.addWidget(self.btn_add_student)
        main_layout.addWidget(self.btn_add_grade)
        main_layout.addWidget(self.btn_produce_reports)
        main_layout.addWidget(self.btn_remove_student)
        main_layout.addWidget(self.btn_settings)

        self.setLayout(main_layout)

    @property
    def class_added_signal(self):
        # This property returns the classAdded signal from the btn_add_class instance
        return self.btn_add_class.classAdded
