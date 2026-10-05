#login window for GUIUniApp
# this is the main window of the GUI application.
# a student types their email and password.
#if they are correct, the enrolment window opens.
# registration is not available in the GUI.
# Only studewnts who already exists in students.data can log in. There are no admin options.
#layout follows a LabelFrame box, StringVar entries and the grid geometry manager inside the frame.
import tkinter as tk

from gui_system.exception_window import ExceptionWindow
from gui_system.enrolment_window import EnrolmentWindow
from student_system.enrolment_controller import EnrolmentController

from student_system.student_controller import StudentController

from utils.exception.student_controller import LoginEmailOrPasswordEmptyError, LoginEmailFormatInvalidError, \
    LoginStudentNotFoundError


class LoginWindow(tk.Tk):
    # the main window where a registered logs in

    def __init__(self, student_controller: StudentController, enrolment_controller: EnrolmentController):
        #database: the Database object, the same on the CLI uses,
        #so both applications read the same students.data

        super().__init__()

        self.student_controller = student_controller
        self.enrolment_controller = enrolment_controller

        self.title("GUIUniApp - Login")
        self.geometry("440x260")
        self.resizable(False,False)

        #StringVar objects hold whatever the user types.
        #We read them later with .get(), as shown in Lec 10.
        self.email_text = tk.StringVar()
        self.password_text = tk.StringVar()

        self.build_widgets()

    def build_widgets(self):
        # create everything the user sees in this window
        heading = tk.Label(self, text="GUIUniApp",font = ("Arial",16))
        heading.pack(pady=(15,5))

        # a labelframe is a box with a title, the fields go inside it.
        box = tk.LabelFrame(self, text = "Student Login", padx=15,pady=10)
        box.pack(padx = 20, pady = 5, fill ="x")

        #inside the box we use grid. the root window uses pack.
        # that is allowed, because they are different containers.
        email_label = tk.Label(box, text = "Email:")
        email_label.grid(row=0,column=0,sticky="w",pady=5)

        email_field = tk.Entry(box, textvariable = self.email_text,width = 30)
        email_field.grid(row=0, column=1, pady=5)

        email_field.focus()

        password_label = tk.Label(box,text = "Password:")
        password_label.grid(row=1,column=0,sticky="w",pady=5)
        password_field = tk.Entry(
            box, textvariable = self.password_text , width = 30, show = "*"
        )
        password_field.grid(row = 1, column = 1, pady = 5)

        login_button = tk.Button(box, text = "Login", width = 10, command = self.login)
        login_button.grid(row=2,column=1,sticky="e",pady=(10,0))

        #Message shown after every action
        self.status_label = tk.Label(self, text = "", fg = "green")
        self.status_label.pack(pady=(8,0))

    def clear(self):
        #empty both entry fields
        self.email_text.set("")
        self.password_text.set("")

    def show_message(self,message,colour = "green"):
        #show a short messg att the bottom of the login window.
        self.status_label.config(text=message, fg = colour)

    def login(self):
        #check what the stud typed and log them in if its correct

        #three diff errors are handled here:
        #one or both fields r empty
        # the email not in correct format
        # no stud with that email and pass exists.

        try:
            email = self.email_text.get().strip()
            password = self.password_text.get()

            student, error = self.student_controller.login_gui(email, password)
            if error is not None:
                self.show_message("Login failed", "red")
                raise error

            # lecture 10 clears the fields after successful login.
            self.clear()
            # hide the login window and open the enrolment window.
            self.withdraw()

            self.enrolment_controller.student = student
            EnrolmentWindow(self, self.enrolment_controller)

        except LoginEmailOrPasswordEmptyError:
            ExceptionWindow(
                self,
                "Missing Details",
                "Please enter both your email and your password.",
            )
            return
        except LoginEmailFormatInvalidError:
            self.show_message("Login failed", "red")
            ExceptionWindow(
                self,
                "Invalid Email",
                "Incorrect email format.\n\n"
                "Emails must look like:\n"
                "firstname.lastname@university.com",
            )
            return
        except LoginStudentNotFoundError:
            self.show_message("Login failed", "red")
            ExceptionWindow(
                self,
                "Login Failed",
                "Incorrect email or password.\n\n"
                "Only registered students can use GUIUniApp.",
            )
            return
        except Exception as e:
            print(f"error logging in in login window: {e}")
            return

#Login worked. the database gives us a dictionary, so turn it
        #into a Student object before passing it on.