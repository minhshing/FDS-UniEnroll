import unittest
from unittest.mock import patch

import gui_main

class GuiMainTest(unittest.TestCase):
    def setUp(self):
        self.database_cls = self.start_patch("gui_main.Database")
        self.student_controller_cls = self.start_patch("gui_main.StudentController")
        self.enrolment_controller_cls = self.start_patch("gui_main.EnrolmentController")
        self.login_window_cls = self.start_patch("gui_main.LoginWindow")

    def start_patch(self, target):
        patcher = patch(target)
        self.addCleanup(patcher.stop)
        return patcher.start()

    def test_database_uses_shared_file(self):
        gui_main.main()

        self.database_cls.assert_called_once_with(filename="students.data")

    def test_controllers_wired_to_database(self):
        gui_main.main()

        database = self.database_cls.return_value
        self.student_controller_cls.assert_called_once_with(database)
        self.enrolment_controller_cls.assert_called_once_with(None, database=database)

    def test_login_window_created_and_mainloop_started(self):
        gui_main.main()

        self.login_window_cls.assert_called_once_with(
            self.student_controller_cls.return_value,
            self.enrolment_controller_cls.return_value,
        )
        self.login_window_cls.return_value.mainloop.assert_called_once()
