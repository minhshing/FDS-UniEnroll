#entry poiint for GUIUniApp
#run this file to start the gui app
# python3 gui_main.py
#guiuniapp uses the same students.data file as cli app
#so any stud registered through the cli can login here.
from database.database import Database
from gui_system.login_window import LoginWindow

def main():
    # the same file the CLI uses, so both applications share the data.
    database = Database(filename="students.data")
    login_window = LoginWindow(database)
    login_window.mainloop()

if __name__ == "__main__":
    main()
