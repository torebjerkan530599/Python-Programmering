from pathlib import Path
import random

# List of last names
last_names = ["Brown", "Smith", "Wolf", "Morse", "Rogers"]

# Function to generate random title and gender
def generate_title_and_gender():
    gender = random.choice(["male", "female"])
    if gender == "male":
        return "Mr", "male"
    else:
        return "Mrs", "female"

# Function to generate random score
def generate_score():
    return random.randint(0, 100)

# Generate data and save to file
input_filename = Path(__file__).parent / "Scores.txt"
with open(input_filename, "w") as file:
    for _ in range(1000):
        title, gender = generate_title_and_gender()
        last_name = random.choice(last_names)
        score = generate_score()
        line = f"{title} {last_name} - Score: {score}%\n"
        file.write(line)
