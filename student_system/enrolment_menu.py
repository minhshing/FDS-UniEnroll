#(c/e/r/s/x) menu a student sees after loggin in.
#printing and all input() calls happen in this file.
#the work is passed to enrolment controller.


from utils.exception.enrolment_exceptions import (
    EnrolmentLimitError,
    SubjectNotFoundError
)

# giving some added colour flairs to the terminal to match the sample output.
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

class EnrolmentMenu:

    def __init__(self, controller):
        self.controller = controller

    def run(self):

        while True:
            choice = input(
                CYAN + "\t\tStudent Course Menu (c/e/r/s/x): " + RESET
            )
            choice = choice.strip().lower()

            if choice == "c":
                self.change_password()
            elif choice == "e":
                self.enrol()
            elif choice == "r":
                self.remove()
            elif choice == "s":
                self.show()
            elif choice == "x":
                break
            else:
                print(RED + "\t\tInvalid choice" + RESET)


    def enrol(self):

        try:
            new_subject = self.controller.enrol()
        except EnrolmentLimitError as error:
            print(RED + "\t\t" + str(error) + RESET)
            return

        print(YELLOW + "\t\tEnrolling in Subject-" + new_subject.id + RESET)
        self.print_enrolment_count()


    def remove(self):
 
        subject_id = input("\t\tRemove Subject by ID: ").strip()

        try:
            self.controller.remove(subject_id)
        except SubjectNotFoundError as error:
            print(RED + "\t\t" + str(error) + RESET)
            return

        print(YELLOW + "\t\tDropping Subject-" + subject_id + RESET)
        self.print_enrolment_count()



    def show(self):

        subjects = self.controller.get_subjects()

        print(YELLOW + "\t\tShowing " + str(len(subjects)) + " subjects" + RESET)

        for subject in subjects:
            print("\t\t" + str(subject))


    def change_password(self):
        print(YELLOW + "\t\tUpdating Password" + RESET)
        new_password = input("\t\tNew Password: ")

        # Keep asking for the confirmation until it matches.
        while True:
            confirm_password = input("\t\tConfirm Password: ")
            if confirm_password == new_password:
                break
            print(RED + "\t\tPassword does not match - try again" + RESET)

        self.controller.change_password(new_password)



    def print_enrolment_count(self):

        count = self.controller.count_subjects()
        print(
            YELLOW + "\t\tYou are now enrolled in " + str(count)
            + " out of 4 subjects" + RESET
        )