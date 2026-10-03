#subs window for GUIUniApp
#lists every subs the stud is enrolled in, with its id, mark and grade

import tkinter as tk

class SubjectWindow(tk.Toplevel):
    #a window listing the student's enrolled subjects.

    def __init__(self,parent,subjects):
        #parent: the enrolment window
        #subjects: the list of Subject objects to display

        super().__init__(parent)

        self.title("GUIUniApp - My Subjects")
        self.geometry("340x280")
        self.resizable(False,False)
        self.transient(parent)

        heading = tk.Label(self, text = "Enrolled Subjects", font = ("Arial", 14))
        heading.pack(pady=(15,10))
        #column headings, so numbers underneath makes sense

        header_row = tk.Label(
            self,
            text="   ID        Mark      Grade",
            font=("Courier",11,"bold"),
        )
        header_row.pack()
        #one line per subject,
        #courier is a fixed width font
        #so the columns line up neatly underneath each other

        for subject in subjects:
            line = (
                " "+subject.id
                +"        "+str(subject.mark).rjust(3)
                +"         "+subject.grade
            )
            row_label = tk.Label(self,text=line, font=("Courier",11))
            row_label.pack()

        total_label = tk.Label(
            self,
            text="Total: "+str(len(subjects))+" out of 4 subjects",
            pady=10,
        )
        total_label.pack(pady=(12,0))

        close_button = tk.Button(self,text= "Close", width = 10, command = self.destroy)
        close_button.pack(pady=(5,15))