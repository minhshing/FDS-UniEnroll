import random
import re

from models.student import Student

from utils.constants import StudentIdConstants, StudentValidationConstants

from utils.exception.database import CreateStudentError
from utils.exception.student_controller import (LoginGUIError,
                                                LoginEmailOrPasswordEmptyError,
                                                LoginEmailFormatInvalidError,
                                                LoginStudentNotFoundError)


class StudentController:
    def __init__(self, database):
        self.database = database

    def is_valid_credentials(self, email, password):
        email_is_valid = re.match(StudentValidationConstants.EMAIL_PATTERN, email) is not None
        password_is_valid = re.match(StudentValidationConstants.PASSWORD_PATTERN, password) is not None
        return email_is_valid and password_is_valid

    def ask_for_valid_credentials(self):
        while True:
            email = input("\tEmail: ")
            password = input("\tPassword: ")

            if self.is_valid_credentials(email, password):
                print("\temail and password formats acceptable")
                return email, password

            print("\tIncorrect email or password format")

    def generate_unique_id(self):
        while True:
            student_id = f"{random.randint(StudentIdConstants.ID_MIN, StudentIdConstants.ID_MAX):0{StudentIdConstants.ID_LENGTH}d}"
            if self.database.get_student_by_id(student_id) is None:
                return student_id

    def register(self):
        print("\tStudent Sign Up")
        email, password = self.ask_for_valid_credentials()

        existing_student = self.database.get_student_by_email(email)
        if existing_student is not None:
            print(f"\tStudent {existing_student['name']} already exists")
            return

        name = ""
        while name == "":
            name = input("\tName: ").strip()

        new_student = Student(self.generate_unique_id(), name, email, password)
        try:
            self.database.create_student(new_student.convert_to_file_data())
            print(f"\tEnrolling Student {name}")
        except CreateStudentError:
            print("\tCould not save student, please try again")

    def login(self):
        print("\tStudent Sign In")
        email, password = self.ask_for_valid_credentials()

        student_data = self.database.get_student_by_email(email)
        if student_data is None or student_data["password"] != password:
            print("\tStudent does not exist")
            return None

        return Student.create_from_file_data(student_data)

    def login_gui(self, email, password):
        try:
            if email == "" or password == "":
                raise LoginEmailOrPasswordEmptyError

            is_email_valid = re.match(StudentValidationConstants.EMAIL_PATTERN, email) is not None
            if not is_email_valid:
                raise LoginEmailFormatInvalidError

            student = self.database.get_student_by_email(email)
            if student is None or student["password"] != password:
                raise LoginStudentNotFoundError

            return Student.create_from_file_data(student)
        except Exception as e:
            print(f"error loging in using GUI: {e}")
            return LoginGUIError