# FDS-UniEnroll
University enrolment system for UTS 32555 Fundamentals of Software Development, Assessment 1 Part 2.
Cmp1-07 Group 3.


#Willy 
- added the student login and register feature for the CLI
- a successful login opens the enrolment menu for that student.
- `StudentController` now takes the database, so `main.py` passes it in.
- change the password pattern based on the requirements, it is now
  `^[A-Z][a-zA-Z]{4,}[0-9]{3,}$`
- added `save_student()` in `student_system/enrolment_controller.py`
- `calculate_average_mark_and_grade()` returns the mark and the grade as a pair
  instead of writing `average_mark` and `average_grade`


## Running

Run both from the project root.

```bash
python3 main.py        # CLIUniApp
python3 gui_main.py    # GUIUniApp


```


