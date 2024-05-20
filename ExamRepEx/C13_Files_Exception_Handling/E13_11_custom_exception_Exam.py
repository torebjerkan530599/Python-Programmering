class ExamException(Exception):
    pass

class NegativeResultException(ExamException):
    pass

class ExcessiveResultException(ExamException):
    pass

class Exam:
    def __init__(self, name, score):
        self.name = name
        if score < 0:
            raise NegativeResultException("Negative exam score is not allowed.")
        elif score > 100:
            raise ExcessiveResultException("Exam score cannot be higher than 100.")
        self.score = score

# Test program
try:
    # Creating an Exam instance with valid score
    exam1 = Exam("Alice", 85)
    print(exam1.name, exam1.score)  # Output: Alice 85

    # Attempting to create an Exam instance with invalid scores
    exam2 = Exam("Bob", -10)  # This will raise a NegativeResultException
except NegativeResultException as e:
    print("Error:", e)
except ExcessiveResultException as e:
    print("Error:", e)

try:
    exam3 = Exam("Charlie", 110)  # This will raise an ExcessiveResultException
except NegativeResultException as e:
    print("Error:", e)
except ExcessiveResultException as e:
    print("Error:", e)
