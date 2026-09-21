from student_system.student_controller import StudentController

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
