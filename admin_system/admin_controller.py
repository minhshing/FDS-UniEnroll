from database.database import Database

from models.subject import calculate_grade
from utils.constants import MarkThresholdConstants, PassThresholdConstants
from utils.exception.admin_controller import (ClearDatabaseError,
                                              GroupStudentsError,
                                              PartitionStudentsError,
                                              RemoveStudentError, ShowStudentsError)

def generate_output_string_from_students(students):
    output_string = ""

    for student in students:
        average_mark, average_grade = calculate_average_mark_and_grade(student)

        name = student["name"]
        id = student["id"]

        output_string += f"{name} :: {id} --> GRADE: {average_grade} - MARK: {average_mark}, "

    # remove the ", " at the end
    output_string = output_string[:-2]
    return output_string

# return the student's average mark and the grade that goes with it.
# this does not touch the student dict, because get_all_students hands out
# the live records and anything written here would end up in students.data.
def calculate_average_mark_and_grade(student):
    subjects = student["subjects"]

    total_mark = 0
    for subject in subjects:
        mark = subject["mark"]
        total_mark += mark

    # a student with no subjects has no marks to average
    if len(subjects) == 0:
        average_mark = 0.0
    else:
        average_mark = total_mark / len(subjects)

    return average_mark, calculate_grade(average_mark)

class AdminController:
    def __init__(self, database: Database):
        self.database = database

    def clear_database(self):
        try:
            self.database.delete_all_students()
            print("successfully cleared database")
        except Exception as e:
            print("error clearing database: " + str(e))
            raise ClearDatabaseError

    def group_students(self):
        try:
            print("GRADE GROUPING")

            students = self.database.get_all_students()

            if len(students) == 0:
                print("<Nothing to display>")
            else:
                z_students = []
                p_students = []
                c_students = []
                d_students = []
                hd_students = []

                for student in students:
                    average_mark, _ = calculate_average_mark_and_grade(student)

                    if average_mark < MarkThresholdConstants.Z_NUMBER:
                        z_students.append(student)
                    elif average_mark < MarkThresholdConstants.P_NUMBER:
                        p_students.append(student)
                    elif average_mark < MarkThresholdConstants.C_NUMBER:
                        c_students.append(student)
                    elif average_mark < MarkThresholdConstants.D_NUMBER:
                        d_students.append(student)
                    else:
                        hd_students.append(student)

                if len(z_students) > 0:
                    output_string = generate_output_string_from_students(z_students)
                    print(f"{MarkThresholdConstants.Z_STRING} -- > [{output_string}]")

                if len(p_students) > 0:
                    output_string = generate_output_string_from_students(p_students)
                    print(f"{MarkThresholdConstants.P_STRING} --> [{output_string}]")

                if len(c_students) > 0:
                    output_string = generate_output_string_from_students(c_students)
                    print(f"{MarkThresholdConstants.C_STRING} --> [{output_string}]")

                if len(d_students) > 0:
                    output_string = generate_output_string_from_students(d_students)
                    print(f"{MarkThresholdConstants.D_STRING} --> [{output_string}]")

                if len(hd_students) > 0:
                    output_string = generate_output_string_from_students(hd_students)
                    print(f"{MarkThresholdConstants.HD_STRING} --> [{output_string}]")


        except Exception as e:
            print("error grouping students: " + str(e))
            raise GroupStudentsError

    def partition_student(self):
        try:
            print("PASS/FAIL PARTITIONING")

            students = self.database.get_all_students()

            pass_students = []
            fail_students = []

            for student in students:
                average_mark, _ = calculate_average_mark_and_grade(student)
                if average_mark < PassThresholdConstants.PASS:
                    fail_students.append(student)
                else:
                    pass_students.append(student)

            fail_output_string = ""
            if len(fail_students) > 0:
                fail_output_string = generate_output_string_from_students(fail_students)
            print(f"FAIL --> [{fail_output_string}]")

            pass_output_string = ""
            if len(pass_students) > 0:
                pass_output_string = generate_output_string_from_students(pass_students)
            print(f"PASS --> [{pass_output_string}]")

        except Exception as e:
            print("error partitioning students: " + str(e))
            raise PartitionStudentsError

    def remove_student(self, student_id):
        try:
            student = self.database.get_student_by_id(student_id)

            if student is None:
                print("Student does not exist")
            else:
                self.database.delete_student(student_id)
        except Exception as e:
            print("error removing student: " + str(e))
            raise RemoveStudentError

    def show_students(self):
        try:
            students = self.database.get_all_students()
            if len(students) == 0:
                print("<Nothing to display>")
            else:
                output_string = generate_output_string_from_students(students)
                print(f"[{output_string}]")
        except Exception as e:
            print("error show: " + str(e))
            raise ShowStudentsError
