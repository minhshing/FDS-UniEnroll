import json
from pathlib import Path

from utils.exception.database import (CreateDatabaseFileError,
                             LoadStudentDataError,
                             CreateStudentError,
                             UpdateStudentError,
                             GetStudentByIdError,
                             GetStudentByEmailError,
                             DeleteStudentError,
                             DeleteAllStudentsError,
                             SaveStudentsError)


class Database:
    students = []

    def __init__(self, filename):
        self.file = Path(filename)

        if not self.file.exists():
            try:
                self.file.write_text("[]", encoding="utf-8")
            except Exception as e:
                print("error creating database file: " + str(e))
                raise CreateDatabaseFileError

        # load students
        try:
            with self.file.open("r", encoding="utf-8") as student_data:
                records = json.load(student_data)

                for record in records:
                    self.students.append(record)
        except Exception as e:
            print("error loading database file: " + str(e))
            raise LoadStudentDataError

    def save_students(self):
        try:
            self.file.write_text(json.dumps(self.students), encoding="utf-8")
        except Exception as e:
            print("error saving students: " + str(e))
            raise SaveStudentsError

    def create_student(self, student):
        try:
            self.students.append(student)
            self.save_students()
        except Exception as e:
            print("error creating student: " + str(e))
            raise CreateStudentError

    def get_all_students(self):
        return self.students

    def get_student_by_id(self, id):
        try:
            for student in self.students:
                if student["id"] == id:
                    return student

            return None
        except Exception as e:
            print("error getting student by id: " + str(e))
            raise GetStudentByIdError

    def get_student_by_email(self, email):
        try:
            for student in self.students:
                if student["email"] == email:
                    return student

            return None
        except Exception as e:
            print("error getting student by email: " + str(e))
            raise GetStudentByEmailError

    def update_student(self, id, student):
        try:
            for index, student in enumerate(self.students):
                if student["id"] == id:
                    self.students[index] = student
                    break

            self.save_students()
        except Exception as e:
            print("error updating student: " + str(e))
            raise UpdateStudentError

    def delete_student(self, id):
        try:
            for index, student in enumerate(self.students):
                if student["id"] == id:
                    self.students.pop(index)
                    break

            self.save_students()
        except Exception as e:
            print("error deleting student: " + str(e))
            raise DeleteStudentError

    def delete_all_students(self):
        try:
            self.students = []
            self.save_students()
        except Exception as e:
            print("error deleting all students: " + str(e))
            raise DeleteAllStudentsError
