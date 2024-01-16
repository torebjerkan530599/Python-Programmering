# This program creates a Car object, a Truck object,
# and an SUV object
import os.path
import pickle
from pathlib import Path
from Car import Car
from Suv import Suv
from Truck import Truck



# Constants for the menu choices
class Codes:
    NEW_CAR_CHOICE = 1
    NEW_TRUCK_CHOICE = 2
    NEW_SUV_CHOICE = 3
    FIND_VEHICLE_CHOICE = 4
    SHOW_VEHICLES_CHOICE = 5
    QUIT_CHOICE = 6

# se 'with - as context manager for filer.pdf'
try:
    path = Path(__file__).parent / "vehicles.txt"
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print('file not found')

def main():
    # Create empty list for vehicles
    #file = 'vehicles.txt'
    #if os.path.isfile(file):
    #vehicles_list = [] # dekker uansett kravet om en tom liste dersom filen ikke eksisterer fylles den ikke
    
    while True:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))
        switch(choice)


        # Perform the selected action.
        # if choice == NEW_CAR_CHOICE:
        #     print('Add a new car')
        # elif choice == NEW_TRUCK_CHOICE:
        #     print('Add a new truck')
        # elif choice == NEW_SUV_CHOICE:
        #     print('Add a new SUV')
        # elif choice == FIND_VEHICLE_CHOICE:
        #     print('Find vehicle by name')
        # elif choice == SHOW_VEHICLES_CHOICE:
        #     #show all vehicles
        #     print('The following cars are in inventory:')
        #     for item in vehicles_list:
        #         if item is car:
        #             print(car)
        #         elif item is truck:
        #             print(truck)
        #         else:
        #             print(suv)
        # elif choice == QUIT_CHOICE:
        #     print('Exiting the program...')    
        # else:
        #     print('Error: invalid selection.')    

# The display_menu function displays a menu.
def display_menu():
    print('\n')
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')
    print()
    
def switch(choice):
    
    match choice:
        case Codes.NEW_CAR_CHOICE:
            print('Add a new car')
        case Codes.NEW_TRUCK_CHOICE:
            print('Add a new truck')
        case Codes.NEW_SUV_CHOICE:
            print('Add a new SUV')
        case Codes.FIND_VEHICLE_CHOICE:
            name = input('Find vehicle by name: ')
            vehicles = [line for line in content.splitlines() if line.startswith(name)]
            if(vehicles):
                [print(line) for line in vehicles]
            else:
                print('No vehicles found...')
        case Codes.SHOW_VEHICLES_CHOICE:
            print('The following cars are in inventory:')
            [print(line) for line in content.splitlines()]
        case Codes.QUIT_CHOICE:
            vehicles = [line for line in content.splitlines()]
            vehicles.sort()
            # Oppgave: Når programmet avsluttes så skal alle kjøretøy sorteres og skrives til fil (pickle / unpickle)
            outputfile = open(Path(__file__).parent / 'vehicles.dat',"wb")
            for v in vehicles:
                pickle.dump(v,outputfile)
            outputfile.close()
            
            # les fra binærfilen
            
            exit('Exiting the program...')
        case _:  
            print('Error: invalid selection.') 

# Call the main function.
if __name__ == '__main__':
      main()