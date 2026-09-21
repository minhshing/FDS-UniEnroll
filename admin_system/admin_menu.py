from utils.constants import AdminMenuInputConstants

class AdminMenu:
    def __init__(self):
        pass

    def run(self):
        while True:
            user_input = input("Admin System (c/g/p/r/s/x): ")
            if user_input == AdminMenuInputConstants.INPUT_CLEAR_DATABASE:
                print("clear db")
            elif user_input == AdminMenuInputConstants.INPUT_GROUP_STUDENTS:
                print("group students")
            elif user_input == AdminMenuInputConstants.INPUT_PARTITION_STUDENTS:
                print("partition students")
            elif user_input == AdminMenuInputConstants.INPUT_REMOVE_STUDENT:
                print("remove student")
            elif user_input == AdminMenuInputConstants.INPUT_SHOW:
                print("show")
            elif user_input == AdminMenuInputConstants.INPUT_EXIT:
                break
            else:
                print("invalid input")
