#handles the printing and typing
#changing the students data and saving it to students.data
#making file alwasy up to date.

from models.subject import create_new_subject, pad_id
from utils.exception.enrolment_exceptions import (
    EnrolmentLimitError,
    SubjectNotFoundError,
)

MAX_SUBJECTS = 4

#enrolment work for one logged in stud
#stud: Student object of the person who just loggd in
#database: Database objectm used to save changes to the file
class EnrolmentController:
    def __init__(self,student,database):
        self.student = student
        self.database = database
    def get_subjects(self):
        #returns a list of subjects the student  has.
        return self.student.subjects
    def count_subjects(self):
        #returns how many subj the student has
        return len(self.student.subjects)
    
    #enrol the subj in one new subj
    #raises enrol limit error if they already hav 4 subjs.
    #returns the new subj so the menu can print it.

    def enrol(self):
        
        #checkin the limit first.
        if self.count_subjects() >= MAX_SUBJECTS:
            raise EnrolmentLimitError (
                "Students are allowed to enrol in 4 Subjects only."
            )
        
        #Collect the ids the studs already has so the new id is different. 
        existing_ids = []
        for subject in self.student.subjects:
            existing_ids.append(subject.id)
        
        new_subject = create_new_subject(existing_ids)
        self.student.subjects.append(new_subject)

        #saving this to student.data straight away.
        self.database.update_student(self.student)
        return new_subject
    
    def remove(self, subject_id):
        #removing one subject by its id, and raising an error if stud has no subj id has it with him.
        #student might have type 97 instead of 097 so padding it
        wanted_id = pad_id(subject_id)

        #look through the students subjects for a matching id.

        subject_to_remove = None
        for subject in self.student.subjects:
            if subject.id == wanted_id:
                subject_to_remove = subject

        if subject_to_remove is None:
            raise SubjectNotFoundError(
                "Subject " + str(subject_id) + " does not exist"
            )
        self.student.subjects.remove(subject_to_remove)

        #saving to students.data straight away.
        self.database.update_student(self.student)
    # changing the students password and saving it.
    def change_password(self, new_password):
        self.student.password = new_password
        self.database.update_student(self.student)




