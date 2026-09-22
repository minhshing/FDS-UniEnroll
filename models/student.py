class Student:
    def __init__(self, student_id, name, email, password, subjects=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects if subjects is not None else []

    def convert_to_file_data(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": self.subjects,
        }

    @classmethod
    def create_from_file_data(cls, student_data):
        return cls(
            student_data["id"],
            student_data["name"],
            student_data["email"],
            student_data["password"],
            student_data["subjects"],
        )
        