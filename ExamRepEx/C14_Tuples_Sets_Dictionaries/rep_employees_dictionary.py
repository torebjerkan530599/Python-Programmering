# Gaddis: Programming Exercise 10-7
# This exercise use the Employee class in emp.py
# Create a program that stores Employee objects in a dictionary.
# Use the employee ID number as the key.
# The program should present a menu that lets the user perform the following actions:
#
# 1. Look up an employee in the dictionary
# 2. Add a new employee to the dictionary
# 3. Change an existing employee’s name, department, and job title in the dictionary
# 4. Delete an employee from the dictionary
# 5. List existing employees
# 6. Quit the program
#
# When the program ends, it should pickle the dictionary and save it to 
# a file. Each time the program starts, it should try to load the 
# pickled dictionary from the file. If the file does not exist, the 
# program should start with an empty dictionary.
import pickle

class Employee:
    def __init__(self, name, id_number, department, title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title
    
    def get_name(self):
        return self.__name
        
    def get_id_number(self):
        return self.__id_number
        
    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    def __str__(self):
        result = 'Name: ' + self.get_name() + \
                 ' ID number: ' + self.get_id_number() + \
                 ' Department: ' + self.get_department() + \
                 ' Title: ' + self.get_title()
        return result

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW = 5
QUIT = 6

# Global constant for filename
FILENAME = 'employees.dat'

# main function
def main():

    # Get employee dictionary.
    employees = load_employees()

    # Initialize variable for user choice.
    choice = 0

    # Process user requests until user quits.
    while choice != QUIT:

        choice = get_user_choice()

        if choice== LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)
        elif choice == SHOW:
            show(employees)

    # Pickle the resulting dictionary.
    save_employees(employees)
    
def load_employees():
    try:
        # Open the file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employee_dict = pickle.load(input_file)

        # Close the file.
        input_file.close()
    except IOError:
        # Could not open file.
        # Create empty dictionary.
        employee_dict = {}

    return employee_dict

def get_user_choice():

    # Display menu, get user choice, and validate it.
    print()
    print('Menu')
    print('----------------------------------------')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Show employees')
    print('6. Quit the program')
    print()

    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('The choice you entered is invalid.'
                           ' Please enter a valid choice: '))

    # Return user's choice.
    return choice

def look_up(employees):
    # Get an employee ID number to look up.
    ID = input('Enter an employee ID number: ')

    # Look ID up in the dictionary. If found,
    # data will print using employee __str__ method
    # otherwise will print specified message.
    print(employees.get(ID, "The specified ID number was not found"))

def add(employees):
    # Get employee information.
    name = input('Enter employee name: ')
    ID = input('Enter employee ID number: ')
    department = input('Enter employee department: ')
    title = input('Enter employee title: ')

    new_emp = Employee(name, ID, department, title)

    # Add new employee if ID does not exist.
    # otherwise notify user that ID exists.
    if ID not in employees:
        employees[ID] = new_emp
        print('The new employee has been added.')
    else:
        print('An employee with that ID already exists.')

def change(employees):
    # Get employee updated information.
    ID = input('Enter employee ID number: ')

    # Change employee information if ID exists.
    # Otherwise, notify user that ID does not exist.
    if ID in employees:
        name = input('Enter the new name: ')
        department = input('Enter the new department: ')
        title = input('Enter the new title: ')

        new_emp = Employee(name, ID, department, title)

        employees[ID] = new_emp
        print('Employee information updated.')
    # ID not found.
    else: 
        print('The specified ID number was not found.')


def delete(employees):
    # Get employee updated information.
    ID = input('Enter employee ID number: ')

    # Change employee information if ID exists.
    # Otherwise, notify user that ID does not exist.
    if ID in employees:
        del employees[ID]
        print('Employee information deleted.')
    # ID not found.
    else: 
        print('The specified ID number was not found.')

def show(employees):
    if len(employees) == 0:
        print("No employees registred")
    else:
        for values in employees.values():
            print(values)
        

# Function pickles the specified dictionary and
# saves it to the employees file.
def save_employees(employees):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(employees, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
if __name__ == '__main__':
    main()

