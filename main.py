from database.database import Database

from admin_system.admin_controller import AdminController
from student_system.student_controller import StudentController

from student_system.student_menu import StudentMenu
from admin_system.admin_menu import AdminMenu

from utils.constants import MainInputConstants


def main():
    # Init db
    database = Database(filename="students.data")

    # Init controllers
    student_controller = StudentController()
    admin_controller = AdminController(database)

    # Init menus
    student_menu = StudentMenu(student_controller)
    admin_menu = AdminMenu(admin_controller)

    # Main loop
    while True:
        user_input = input("University System: (A)dmin, (S)tudent, or X : ")
        if user_input == MainInputConstants.INPUT_STUDENT_SYSTEM:
            student_menu.run()
        elif user_input == MainInputConstants.INPUT_ADMIN_SYSTEM:
            admin_menu.run()
        elif user_input == MainInputConstants.INPUT_EXIT:
            print("Thank you")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()