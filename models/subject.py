#every subject has an 
# id (3 digits stored as text like "034")
# a mark (a no. between 25 to 100)

import random

BIGGEST_ID = 999
SMALLEST_ID = 1
ID_LENGTH = 3

BIGGEST_MARK = 100
SMALLEST_MARK = 25

#helper functions

def pad_id(number): #suppose a number 54 is converted to a 3 digit text id like "054"
    return str(number).zfill(ID_LENGTH)


#uts grade distribution
# mark < 50 is Z, mark 50 to <65 is P, mark 65 to below 75 is C, mark 75 to 85 is D, mark 85 or more is HD
# the mark can be a whole number relating to one subject or a decimal, (like the avg mark)

def calculate_grade(mark):
    if mark >= 85:
        return "HD"
    elif mark >= 75:
        return "D"
    elif mark >= 65:
        return "C"
    elif mark >= 50:
        return "P"
    
    else:
        return "Z"

# -> making a random 3 digit id that is not already used
# existing_ids is a list of ids the student already has, for ex: having subjects ['231','324']
# we are trying to build a list of every id that is still free, and pick one of them at random
# this way measn the funtion always finishes , even if nearly every id is taken

#making sure every existing id are padded like 54 -> "054" this matches.

def generate_subject_id(existing_ids):
    used_ids = []
    for one_id in existing_ids:
        used_ids.append(pad_id(one_id))
    
    #collecting every id that is still availble
    free_ids = []
    for number in range(SMALLEST_ID,BIGGEST_ID+1):
        padded = pad_id(number)
        if padded not in used_ids:
            free_ids.append(padded)

    if len(free_ids) ==0:
        raise RuntimeError("There are no subject ids left")
    
    return random.choice(free_ids)


#a random mark betwee 25 to 100

def generate_mark():
    return random.randint(SMALLEST_MARK,BIGGEST_MARK)

# subject class
#one subject that a sutdent is enrolled
#subject_id = 3 digit it as text for ex: "032"
#mark = a number between 25 and 100
#grade = it is only passed in when we load a subject back from students.data.
class Subject:
    def __init__(self, subject_id, mark, grade = None):
        self.id = pad_id(subject_id)
        self.mark = mark

        if grade is None:
            self.grade = calculate_grade(mark)
        else:
            self.grade = grade
    
    def to_dict(self):
        #turining this subj into a dict so it can be saved into students.data as JSON

        return {
            "id": self.id,
            "mark": self.mark,
            "grade": self.grade,

        }

    def __str__(self):
        #it should look like [ Subject::053 -- mark = 93 -- grade = HD ]
        #grade is padded to 3 chars so that "P" and "HD" line up on the same column
        padded_grade = self.grade.rjust(3)
        return "[ Subject::" + self.id + " -- mark = " + str(self.mark) \
                + " -- grade = " + padded_grade + " ]"
    

#    a brand new subj for a stud who enrolling
# the id mark and grade are all generated automatically, cuz student deos not choose any of them
    
def create_new_subject(existing_ids):
    new_id = generate_subject_id(existing_ids)
    new_mark = generate_mark()
    return Subject(new_id, new_mark)

# rebuilding a subj from a dict reads out  of students.data.
def subject_from_dict(data):
    subject_id = data["id"]
    mark = data["mark"]

    #older records might not have a grade saved 
    if "grade" in data:
        grade = data ["grade"]
    else:
        grade = None
    return Subject(subject_id,mark,grade)


    

