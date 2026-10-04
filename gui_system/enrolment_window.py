#enrolment window for guiuniapp
# a logged in stud can enrol in upto four subs here
#and open the subs window to see what they are enrolled in

#this window uses the same EnrolmentController as the CLI application.
# so the four subs limit and the saving to students.data behave.
#exactly the same way in both.

import tkinter as tk
from student_system.enrolment_controller import EnrolmentController
from utils.exception.enrolment_exceptions import EnrolmentLimitError
from gui_system.exception_window import ExceptionWindow
from gui_system.subject_window import SubjectWindow

class EnrolmentWindow(tk.Toplevel):
    #window where a stud enrols in subj
    
    def __init__(self,parent,student,database):
        #parent: the login window
        #student: the Student object of whoever just logged in
        #database: the Database object, used to save changes

        super().__init__(parent)
        self.parent = parent
        self.student = student

        #the same controller the CLI menu uses.
        self.controller = EnrolmentController(student, database)
        self.title("GUIUniApp - Enrolment")
        x_position = parent.winfo_x()
        y_position = parent.winfo_y()
    
        self.geometry("380x300+" + str(x_position)+ "+"+ str(y_position))
        self.resizable(False,False)

        #if the stud closes this window, close the whole app.
        #instead of leaving the hidden login window runing.
        self.protocol("WM_DELETE_WINDOW",self.handle_close)
        self.build_widgets()
        self.update_count_label()

    def build_widgets(self):
        #create everything the user sees in this window.
        heading = tk.Label(
            self,
            text="Welcome " + self.student.name,
            font=("Arial",14),
        )
        heading.pack(pady=(20,5))

        id_label = tk.Label(self,text="Student ID: "+ str(self.student.student_id))
        id_label.pack()

        #show how many subjs out of 4 the stud has.
        self.count_label = tk.Label(self, text="", font=("Arial",12))
        self.count_label.pack(pady=(15,10))

        enrol_button = tk.Button(
            self, text = "Enrol in a Subject", width = 20, command = self.handle_enrol
            )
        enrol_button.pack(pady=5)

        show_button = tk.Button(
            self, text = "Show My Subjects", width = 20, command = self.handle_show
        )

        show_button.pack(pady=5)
        logout_button = tk.Button(
            self,text ="Logout",width=20,command=self.handle_logout
        )
        logout_button.pack(pady=5)

        #message shown after every action
        self.status_label = tk.Label(self, text="", fg="green",wraplength=340)
        self.status_label.pack(pady=(12,0))

    def update_count_label(self):
        #Refresh the line showing how many subs are enrolled
        count = self.controller.count_subjects()
        self.count_label.config(
            text = "Enrolled in " + str(count) + " out of 4 subjects"
        )

    def handle_enrol(self):
        #enrol the stud in one new subj\
        #the controller raises EnrolmentLimitError if the stud already has 4 subs
        # and that is shown in the exception window.

        try:
            new_subject = self.controller.enrol()
        except EnrolmentLimitError as error:
            ExceptionWindow(self,"Enrolment Limit",str(error))
            return
        self.update_count_label()
        self.status_label.config(
            text = "Enrolled in Subject-" + new_subject.id
            +"  (mark " + str(new_subject.mark)
            +", grade " + new_subject.grade + ")",
            fg="green",
        )
    
    def handle_show(self):
        #open the sub window listing all enrolled subs
        subjects = self.controller.get_subjects()

        if len(subjects) == 0:
            ExceptionWindow(
                self,
                "No Subjects",
                "You are not enrolled in any subjects yet.",
            )
            return
        
        SubjectWindow(self,subjects)
        self.status_label.config(text="Showing your enrolled subjects",fg="green")

    def handle_logout(self):
        #close this window and go back to the login window.
        self.parent.deiconify()
        self.parent.show_message("You have logged out", "green")
        self.destroy()

    def handle_close(self):
        #closoing the whole application
        self.parent.destroy()