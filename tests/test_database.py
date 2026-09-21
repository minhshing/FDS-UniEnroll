import json
import os
import unittest

from database.database import Database

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.database = Database("students.data.test")

    def tearDown(self):
        os.remove("students.data.test")

    def test_create_student(self):
        email = "test@gmail.com"
        password = "1234"

        student = {
            "email": email,
            "password": password,
            "id": "000001",
            "name": "Minh Nguyen",
            "subjects": [
                {
                    "id": "001",
                    "mark": 50,
                    "grade": "P"
                }
            ]
        }

        self.database.create_student(student)

        student = self.database.get_student_by_id("000001")
        self.assertEqual(student["email"], email)
        self.assertEqual(student["password"], password)

    def test_save_students(self):
        self.database.students = [
            {
                "email": "test@gmail.com",
                "password": "1234",
                "id": "000001",
                "name": "Minh Nguyen",
                "subjects": [
                    {
                        "id": "001",
                        "mark": 50,
                        "grade": "P"
                    }
                ]
            }
        ]

        self.database.save_students()
        with self.database.file.open("r", encoding="utf-8") as f:
            students = json.load(f)

            self.assertEqual(len(students), 1)
