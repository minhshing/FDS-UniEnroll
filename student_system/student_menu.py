from utils.constants import StudentMenuInputConstants

class StudentMenu:
    def __init__(self):
        pass

    def run(self):
        while True:
            user_input = input("Student system (l/r/x): ")
            if user_input == StudentMenuInputConstants.INPUT_LOGIN:
                print("Student Login")
            elif user_input == StudentMenuInputConstants.INPUT_REGISTER:
                print("Student Register")
            elif user_input == StudentMenuInputConstants.INPUT_EXIT:
                break
            else:
                print("Invalid input")
