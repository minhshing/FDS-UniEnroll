from models.subject import subject_from_dict #<-- Rafeed's code
class Student:
    def __init__(self, student_id, name, email, password, subjects=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects if subjects is not None else []

    def convert_to_file_data(self):
        #Rafeed's code:
        subject_dicts = []
        for subject in self.subjects:
            subject_dicts.append(subject.to_dict())
        return {
            "id": self.student_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            # "subjects": self.subjects, <- willys prev code
            #rafeeds new code
            "subjects": subject_dicts,
        }

    @classmethod
    def create_from_file_data(cls, student_data):
        #Rafeed's code
        subject_objects = []
        for subject_data in student_data["subjects"]:
            subject_objects.append(subject_from_dict(subject_data))
        return cls(
            student_data["id"],
            student_data["name"],
            student_data["email"],
            student_data["password"],
            # student_data["subjects"], <- willys prev code
            #Rafeeds code
            subject_objects,
        )
        