#enrolment rules for one logged in student: enrol, remove, change password.
#every change is saved to students.data straight away.
#printing and input() are done by EnrolmentMenu (CLI) and EnrolmentWindow (GUI).

from models.subject import create_new_subject, pad_id
from utils.constants import SubjectConstants
from utils.exception.enrolment_exceptions import (
    EnrolmentLimitError,
    SubjectNotFoundError,
)

#kept under this name because enrolment_menu.py imports it from here.
MAX_SUBJECTS = SubjectConstants.MAX_SUBJECTS

#enrolment work for one logged in student
#student: Student object of the person who just logged in
#database: Database object, used to save changes to the file
class EnrolmentController:
    def __init__(self, student, database):
        self.student = student
        self.database = database

    def get_subjects(self):
        #returns the list of subjects the student has.
        return self.student.subjects

    def count_subjects(self):
        #returns how many subjects the student has.
        return len(self.student.subjects)

    #enrol the student in one new subject.
    #raises EnrolmentLimitError if they already have MAX_SUBJECTS subjects.
    #returns the new subject so the menu can print it.
    def enrol(self):

        #checking the limit first, so nothing changes when it is reached.
        if self.count_subjects() >= MAX_SUBJECTS:
            raise EnrolmentLimitError(
                "Students are allowed to enrol in " + str(MAX_SUBJECTS) + " subjects only."
            )

        #collect the ids the student already has so the new id is different.
        existing_ids = []
        for subject in self.student.subjects:
            existing_ids.append(subject.id)

        new_subject = create_new_subject(existing_ids)
        self.student.subjects.append(new_subject)

        #saving this to students.data straight away.
        self.save_student()
        return new_subject

    def remove(self, subject_id):
        #remove one subject by its id.
        #raises SubjectNotFoundError if the student does not have that subject.
        #the student might type 97 instead of 097, so the id is padded first.
        wanted_id = pad_id(subject_id)

        #look through the student's subjects for a matching id.
        subject_to_remove = None
        for subject in self.student.subjects:
            if subject.id == wanted_id:
                subject_to_remove = subject
                break

        if subject_to_remove is None:
            raise SubjectNotFoundError(
                "Subject " + str(subject_id) + " does not exist"
            )
        self.student.subjects.remove(subject_to_remove)

        #saving to students.data straight away.
        self.save_student()

    #change the student's password and save it.
    #the menu has already checked the password format.
    def change_password(self, new_password):
        self.student.password = new_password
        self.save_student()

    def save_student(self):
        #write this student back to students.data.
        #the database stores plain dicts, so the Student has to be
        #converted first, and it is matched on its id.
        self.database.update_student(
            self.student.student_id, self.student.convert_to_file_data()
        )

    def get_student_id(self):
        return self.student.student_id

    def get_student_name(self):
        return self.student.name