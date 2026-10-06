#(c/e/r/s/x) menu a student sees after loggin in.
#printing and all input() calls happen in this file.
#the work is passed to enrolment controller.
import re
from student_system.enrolment_controller import MAX_SUBJECTS
from utils.constants import(
    EnrolmentMenuInputConstants,
    StudentValidationConstants,
)

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

            if choice == EnrolmentMenuInputConstants.INPUT_CHANGE_PASSWORD:
                self.change_password()
            elif choice == EnrolmentMenuInputConstants.INPUT_ENROL:
                self.enrol()
            elif choice == EnrolmentMenuInputConstants.INPUT_REMOVE:
                self.remove()
            elif choice == EnrolmentMenuInputConstants.INPUT_SHOW:
                self.show()
            elif choice == EnrolmentMenuInputConstants.INPUT_EXIT:
                break
            else:
                print(RED + "\t\tInvalid choice" + RESET)

#enrol
    def enrol(self):
#enrol in a new sub and print result
        try:
            new_subject = self.controller.enrol()
        except EnrolmentLimitError as error:
            print(RED + "\t\t" + str(error) + RESET)
            return
#sample shows "Subect-97" unpadded here. to match it
#exactly
#replace new_subject.id with str(int(new_subject.id)).
        print(YELLOW + "\t\tEnrolling in Subject-" + new_subject.id + RESET)
        self.print_enrolment_count()


    def remove(self):
 #ask for a sub id and remove that subject
        subject_id = input("\t\tRemove Subject by ID: ").strip()

        try:
            self.controller.remove(subject_id)
        except SubjectNotFoundError as error:
            print(RED + "\t\t" + str(error) + RESET)
            return

        print(YELLOW + "\t\tDropping Subject-" + subject_id + RESET)
        self.print_enrolment_count()



    def show(self):
#print every subs the student is enrolled in
        subjects = self.controller.get_subjects()

        print(YELLOW + "\t\tShowing " + str(len(subjects)) + " subjects" + RESET)

        for subject in subjects:
            print("\t\t" + str(subject))


    def change_password(self):
        #ask for a new pass, check its format, confirm it, then save.
        print(YELLOW + "\t\tUpdating Password" + RESET)

        #keep asking until the password matches the required format.
        while True:
            new_password = input("\t\tNew Password: ")
            if re.match(StudentValidationConstants.PASSWORD_PATTERN,new_password):
                break
            print(RED + "\t\tIncorrect password format"+RESET)

        # Keep asking for the confirmation until it matches.
        #without this, a stud could set a password they can
        #never login with, cuz login checks the same rules.
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
            + " out of " + str(MAX_SUBJECTS)+ " subjects"+  RESET
        )