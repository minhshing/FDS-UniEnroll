from admin_system.admin_controller import AdminController

from utils.constants import AdminMenuInputConstants

class AdminMenu:
    def __init__(self, controller: AdminController):
        self.controller = controller

    def run(self):
        while True:
            user_input = input("Admin System (c/g/p/r/s/x): ")
            if user_input == AdminMenuInputConstants.INPUT_CLEAR_DATABASE:
                self.controller.clear_database()
            elif user_input == AdminMenuInputConstants.INPUT_GROUP_STUDENTS:
                self.controller.group_students()
            elif user_input == AdminMenuInputConstants.INPUT_PARTITION_STUDENTS:
                self.controller.partition_student()
            elif user_input == AdminMenuInputConstants.INPUT_REMOVE_STUDENT:
                student_id = input("REMOVE BY ID: ")
                self.controller.remove_student(student_id)
            elif user_input == AdminMenuInputConstants.INPUT_SHOW:
                self.controller.show_students()
            elif user_input == AdminMenuInputConstants.INPUT_EXIT:
                break
            else:
                print("invalid input")
