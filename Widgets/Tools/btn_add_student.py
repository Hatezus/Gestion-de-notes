from PySide6.QtWidgets import QPushButton, QMessageBox
from pathlib import Path
import json

import Modules.check_module as check_module
import Modules.settings_module as settings_module
import Widgets.Pop_Up.pop_up_add_student as pop_up_add_student


class AddStudentBtn(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.clicked.connect(self.on_click)

    def on_click(self):
        if check_module.check_active_year():
            dialog = pop_up_add_student.AddStudentDialog()
            if dialog.exec_():
                surname_inputed = dialog.input_surname
                firstname_imputed = dialog.input_firstname
                student_name = (f"{surname_inputed}_{firstname_imputed}.json")

                settings = settings_module.load_settings()

                current_class_path = Path(settings["current_class_path"])
                current_student_path = current_class_path / "Students" / student_name

                if not current_student_path.exists():
                    try:
                        current_student_path.touch()
                        with open(current_student_path, 'w', encoding='utf-8') as f:
                            student_data = {
                                "trimester_1" : 
                                    {
                                    "grammaire" : [],
                                    "conjugaison" : [],
                                    "vocabulaire" : [],
                                    "expression_écrite" : [],
                                    "lecture" : [],
                                    "dictées" : [],
                                    "orthographe" : [],
                                    "langue_orale" : [],
                                    "anglais" : [],
                                    "numération" : [],
                                    "géométrie_mesure" : [],
                                    "opération_calcul" : [],
                                    "résolution_de_problèmes" : [],
                                    "thème_1" : [],
                                    "thème_2" : [],
                                    "thème_3" : [],
                                    "participe_volontier" : False,
                                    "participe_après_demande" : False,
                                    "travail_difficilement" : False,
                                    "concentre_difficilement" : False,
                                    "manque_de_confiance" : False,
                                    "soignée" : False,
                                    "correcte" : False,
                                    "irrégulière" : False,
                                    "négligée" : False,
                                    "appréciations" :""
                                    },
                                "trimester_2" : 
                                    {
                                    "grammaire" : [],
                                    "conjugaison" : [],
                                    "vocabulaire" : [],
                                    "expression_écrite" : [],
                                    "lecture" : [],
                                    "dictées" : [],
                                    "orthographe" : [],
                                    "langue_orale" : [],
                                    "anglais" : [],
                                    "numération" : [],
                                    "géométrie_mesure" : [],
                                    "opération_calcul" : [],
                                    "résolution_de_problèmes" : [],
                                    "thème_1" : [],
                                    "thème_2" : [],
                                    "thème_3" : [],
                                    "participe_volontier" : False,
                                    "participe_après_demande" : False,
                                    "travail_difficilement" : False,
                                    "concentre_difficilement" : False,
                                    "manque_de_confiance" : False,
                                    "soignée" : False,
                                    "correcte" : False,
                                    "irrégulière" : False,
                                    "négligée" : False,
                                    "appréciations" :""
                                    },
                                "trimester_3" : 
                                    {
                                    "grammaire" : [],
                                    "conjugaison" : [],
                                    "vocabulaire" : [],
                                    "expression_écrite" : [],
                                    "lecture" : [],
                                    "dictées" : [],
                                    "orthographe" : [],
                                    "langue_orale" : [],
                                    "anglais" : [],
                                    "numération" : [],
                                    "géométrie_mesure" : [],
                                    "opération_calcul" : [],
                                    "résolution_de_problèmes" : [],
                                    "thème_1" : [],
                                    "thème_2" : [],
                                    "thème_3" : [],
                                    "participe_volontier" : False,
                                    "participe_après_demande" : False,
                                    "travail_difficilement" : False,
                                    "concentre_difficilement" : False,
                                    "manque_de_confiance" : False,
                                    "soignée" : False,
                                    "correcte" : False,
                                    "irrégulière" : False,
                                    "négligée" : False,
                                    "appréciations" :""
                                    }
                            }
                            json.dump(student_data, f, ensure_ascii=False, indent=4)
                    except Exception as e:
                        QMessageBox.critical(self, "Error", f"Une erreur est survenue : {str(e)}")
                else:
                     QMessageBox.critical(self, "Error", f"Il existe déja un étudiant avec ce nom et ce prénom")
                    

        else:
            QMessageBox.critical(self, "Error", f"Il n'y à pas d'année en cours")