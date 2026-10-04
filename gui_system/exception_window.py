#exception window for the GUIUniApp.
# this window pops up whenever something goes wrong.
# for ex: empty login, or an attempt to enrol in a fifth subj
# it is one of the four windows required by the marking scheme.

import tkinter as tk

class ExceptionWindow(tk.Toplevel):
    # a small pop up window that shows one error message
    def __init__(self, parent, title, message):
        # parent: the window that opened this one.
        # title: the title shown in the window bar
        # message: the error message to show the user.

        super().__init__(parent)

        self.title(title)
        self.resizable(False,False)
        
        # make this windows sit on top of its parent and block it.
        # so the user has to deal with the error before carrying on.

        self.transient(parent)
        self.grab_set()

        #message label

        message_label = tk.Label(
            self,
            text=message,
            wraplength=260,
            justify = "left",
            padx = 20,
            pady = 20,
        )
        message_label.pack()

        ok_button = tk.Button(self,text = "OK", width = 10, command = self.destroy)
        ok_button.pack(pady=(0,15))

        # wait here until the user closes this window.
        self.wait_window()
        

