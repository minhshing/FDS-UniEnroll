import unittest
from unittest.mock import patch, call

import main
from utils.constants import MainInputConstants

class MainTest(unittest.TestCase):
    def setUp(self):
        self.database_cls = self.start_patch("main.Database")
        self.student_controller_cls = self.start_patch("main.StudentController")
        self.admin_controller_cls = self.start_patch("main.AdminController")
        self.student_menu_cls = self.start_patch("main.StudentMenu")
        self.admin_menu_cls = self.start_patch("main.AdminMenu")
        self.mock_print = self.start_patch("builtins.print")

        self.student_menu = self.student_menu_cls.return_value
        self.admin_menu = self.admin_menu_cls.return_value

    def start_patch(self, target):
        patcher = patch(target)
        self.addCleanup(patcher.stop)
        return patcher.start()

    def run_main(self, inputs):
        with patch("builtins.input", side_effect=inputs):
            main.main()

    def test_wiring(self):
        self.run_main([MainInputConstants.INPUT_EXIT])

        self.database_cls.assert_called_once_with(filename="students.data")
        database = self.database_cls.return_value
        self.student_controller_cls.assert_called_once_with(database)
        self.admin_controller_cls.assert_called_once_with(database)
        self.student_menu_cls.assert_called_once_with(self.student_controller_cls.return_value)
        self.admin_menu_cls.assert_called_once_with(self.admin_controller_cls.return_value)

    def test_exit_prints_thank_you(self):
        self.run_main([MainInputConstants.INPUT_EXIT])

        self.mock_print.assert_called_once_with("Thank You")
        self.student_menu.run.assert_not_called()
        self.admin_menu.run.assert_not_called()

    def test_student_option_runs_student_menu(self):
        self.run_main([MainInputConstants.INPUT_STUDENT_SYSTEM, MainInputConstants.INPUT_EXIT])

        self.student_menu.run.assert_called_once()
        self.admin_menu.run.assert_not_called()

    def test_admin_option_runs_admin_menu(self):
        self.run_main([MainInputConstants.INPUT_ADMIN_SYSTEM, MainInputConstants.INPUT_EXIT])

        self.admin_menu.run.assert_called_once()
        self.student_menu.run.assert_not_called()

    def test_lowercase_and_whitespace_accepted(self):
        self.run_main(["  s ", " a", "x"])

        self.student_menu.run.assert_called_once()
        self.admin_menu.run.assert_called_once()
        self.mock_print.assert_called_once_with("Thank You")

    def test_invalid_input(self):
        self.run_main(["foo", MainInputConstants.INPUT_EXIT])

        self.assertEqual(self.mock_print.call_args_list, [call("Invalid input"), call("Thank You")])
        self.student_menu.run.assert_not_called()
        self.admin_menu.run.assert_not_called()

    def test_multiple_rounds(self):
        self.run_main([
            MainInputConstants.INPUT_STUDENT_SYSTEM,
            MainInputConstants.INPUT_STUDENT_SYSTEM,
            MainInputConstants.INPUT_ADMIN_SYSTEM,
            MainInputConstants.INPUT_EXIT,
        ])

        self.assertEqual(self.student_menu.run.call_count, 2)
        self.assertEqual(self.admin_menu.run.call_count, 1)
