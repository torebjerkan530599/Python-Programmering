# This program creates a Car object, a Truck object,
# and an SUV object
import os.path
import pickle
from pathlib import Path

import Vehicle
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

vehicle_collection = []

def main():
    
    while True:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))
        switch(choice)
    
def switch(choice):
    
    match choice:
        case Codes.NEW_CAR_CHOICE | Codes.NEW_TRUCK_CHOICE | Codes.NEW_SUV_CHOICE:
            vehicle_collection.append(new_vehicle(choice))
            # with open("vehicles.dat", 'wb') as picklefile:
            #     picklefile.write(vehicle_collection)
        case Codes.FIND_VEHICLE_CHOICE:
            name = input('Find vehicle by name: ')
            vehicles = [line for line in content.splitlines() if line.startswith(name)]
            if(vehicles):
                [print(line) for line in vehicles]
            else:
                print('No vehicles found...')
                
                
        # -------------------WIP------------------------------ #
        case Codes.SHOW_VEHICLES_CHOICE:
            print('The following cars are in inventory:')
            inputFile = open(Path(__file__).parent / "vehicles.dat","rb")
            end_of_file = False
            while not end_of_file:
                try:
                    print(pickle.load(inputFile), end = '')
                except EOFError:
                    end_of_file = True
            inputFile.close()
            #[print(line) for line in content.splitlines()]
        # -------------------WIP------------------------------ #
        case Codes.QUIT_CHOICE:
            vehicles = [line for line in content.splitlines()]
            vehicles.sort()
            # Oppgave: Når programmet avsluttes så skal alle kjøretøy sorteres og skrives til fil (pickle / unpickle)
            
            outputfile = open(Path(__file__).parent / 'vehicles.dat',"wb")
            
            with open("vehicles.dat", 'wb') as picklefile:
                picklefile.write(vehicle_collection)
            # for v in vehicles:
            #     pickle.dump(v,outputfile)
            # outputfile.close()
            
            # les fra binærfilen
            
            exit('Exiting the program...')
        case _:  
            print('Error: invalid selection.') 

def new_vehicle(choice):
    # make = input('Enter make: ')
    # model = input('Enter model: ')    
    # mileage = input('Enter milage: ')
    # price = input('Enter price: ')

    make = 'KIA', 
    model = '2003'
    mileage = '20034'
    price = '45959'
    if choice == Codes.NEW_CAR_CHOICE:
        #doors = input('Enter doors: ')
        doors = '4'
        return Vehicle.Car(make,model,mileage,price,doors)
        #print(new_car)
    if choice == Codes.NEW_TRUCK_CHOICE:
        #drive_type = input('Enter drive type: ')
        drive_type = '3D'
        return Vehicle.Truck(make,model,mileage,price,drive_type)
    if choice == Codes.NEW_SUV_CHOICE:
        #passengers = input('Enter passengers: ')
        passengers = '50'
        return Vehicle.Suv(make,model,mileage,price,passengers)

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

# Call the main function.
if __name__ == '__main__':
      main()
      



    # Create empty list for vehicles
    #file = 'vehicles.txt'
    #if os.path.isfile(file):
    #vehicles_list = [] # dekker uansett kravet om en tom liste dersom filen ikke eksisterer fylles den ikke