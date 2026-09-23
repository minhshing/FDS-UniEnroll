# CLI input option
class MainInputConstants:
    INPUT_ADMIN_SYSTEM = "A"
    INPUT_STUDENT_SYSTEM = "S"
    INPUT_EXIT = "X"

class StudentMenuInputConstants:
    INPUT_LOGIN = "l"
    INPUT_REGISTER = "r"
    INPUT_EXIT = "x"

class AdminMenuInputConstants:
    INPUT_CLEAR_DATABASE = "c"
    INPUT_GROUP_STUDENTS = "g"
    INPUT_PARTITION_STUDENTS = "p"
    INPUT_REMOVE_STUDENT = "r"
    INPUT_SHOW = "s"
    INPUT_EXIT = "x"

# Mark threshold
class MarkThresholdConstants:
    Z_NUMBER = 50
    P_NUMBER = 65
    C_NUMBER = 75
    D_NUMBER = 85
    HD_NUMBER = 100

    Z_STRING = "Z"
    P_STRING = "P"
    C_STRING = "C"
    D_STRING = "D"
    HD_STRING = "HD"

class PassThresholdConstants:
    PASS = 50

class StudentValidationConstants:
    EMAIL_PATTERN = r"^[a-zA-Z]+\.[a-zA-Z]+@university\.com$"
    PASSWORD_PATTERN = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$"

class StudentIdConstants:
    ID_MIN = 1
    ID_MAX = 999999
    ID_LENGTH = 6