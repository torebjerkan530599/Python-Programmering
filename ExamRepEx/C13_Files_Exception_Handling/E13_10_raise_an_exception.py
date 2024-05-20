class Exam:
    def __init__(self, name, score):
        self.name = name
        if score < 0 or score > 100:
            raise RuntimeError("Score must be between 0 and 100.")
        self.score = score

# Example usage:
try:
    # Creating an Exam instance with valid score
    exam1 = Exam("Alice", 85)
    print(exam1.name, exam1.score)  # Output: Alice 85

    # Attempting to create an Exam instance with invalid score
    exam2 = Exam("Bob", -10)  # This will raise a RuntimeError
except RuntimeError as e:
    print("Error:", e)
