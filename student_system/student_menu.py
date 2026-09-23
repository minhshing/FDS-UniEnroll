from student_system.student_controller import StudentController

# Rafeed's code - Subject Enrolment System
from student_system.enrolment_controller import EnrolmentController
from student_system.enrolment_menu import EnrolmentMenu

from utils.constants import StudentMenuInputConstants


class StudentMenu:
    def __init__(self, controller: StudentController):
        self.controller = controller

    def run(self):
        while True:
            user_input = input("Student system (l/r/x): ")
            if user_input == StudentMenuInputConstants.INPUT_LOGIN:
                #TODO: implement controller logic for student login
                pass
            elif user_input == StudentMenuInputConstants.INPUT_REGISTER:
                #TODO: implement controller logic for student register
                pass
            elif user_input == StudentMenuInputConstants.INPUT_EXIT:
                break
            else:
                print("Invalid input")


# Rafeeds code- enrolment menu system
    def open_enrolment_menu(self, student):

        enrolment_controller = EnrolmentController(
            student, self.controller.database
        )
        enrolment_menu = EnrolmentMenu(enrolment_controller)
        enrolment_menu.run()