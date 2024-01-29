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
# try:
#     path = Path(__file__).parent / "vehicles.txt"
#     content = path.read_text(encoding="utf-8")
# except FileNotFoundError:
#     print('file not found')

# A collection of vehicles to be written to file initially for testing purposes
vehicle_collection = [Vehicle.Car('BMW 320', '2001', '70000', '15000.0' , '4'), 
                      Vehicle.Suv('Volvo XC60', '2010', ' 30000' , ' 18500.0', 5), 
                      Vehicle.Truck('Toyota RAV4', '2002', '40000', '12000.0', '4WD')]
        

def main():
    
    #switch(1) # for testing purposes, write vehicle_collection to file and add a new car 
    with open('vehicles.dat', 'wb') as picklefile:
        pickle.dump(vehicle_collection, picklefile)
    
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
            with open('vehicles.dat', 'wb') as picklefile:
                 pickle.dump(vehicle_collection, picklefile)
            
        case Codes.FIND_VEHICLE_CHOICE:
            name = input('Find vehicle by name: ')
            with open('vehicles.dat', 'rb') as file:
                objects = pickle.load(file)
            
            for vehcile in objects:
                    if str(vehcile._make).startswith(name):
                        print(vehcile)
                
        # -------------------WIP------------------------------ #
        case Codes.SHOW_VEHICLES_CHOICE:
            print('The following cars are in inventory:')
            
            try: # test if file exists...
                inputFile = open("vehicles.dat","rb")
            except FileNotFoundError: #...create if not
                inputFile = open("vehicles.dat","wb")
                
            objects = []
            end_of_file = False
            while not end_of_file:
                try:
                    objects = pickle.load(inputFile)
                except EOFError:
                    end_of_file = True
            inputFile.close()
            
            for o in objects:
                print(o)
        # -------------------WIP------------------------------ #
        case Codes.QUIT_CHOICE:
            vehicle_collection_sorted = sorted(vehicle_collection, key=lambda vehicle: vehicle._make, reverse=False)
            
            #skriv
            with open('vehicles.dat','wb') as file:
                    pickle.dump(vehicle_collection_sorted,file)
            
            objects = []
            
            # les
            print('Vehicles written to file: ')
            with open('vehicles.dat', 'rb') as file:
                objects = pickle.load(file)
            
            for o in objects:
                print(o)
                    
            exit('Exiting the program...')
        case _:  
            print('Error: invalid selection.') 

def new_vehicle(choice):
    make = input('Enter make: ')
    model = input('Enter model: ')    
    mileage = input('Enter milage: ')
    price = input('Enter price: ')
    
    if choice == Codes.NEW_CAR_CHOICE:
        doors = input('Enter doors: ')
        return Vehicle.Car(make,model,mileage,price,doors)
    if choice == Codes.NEW_TRUCK_CHOICE:
        drive_type = input('Enter drive type: ')
        return Vehicle.Truck(make,model,mileage,price,drive_type)
    if choice == Codes.NEW_SUV_CHOICE:
        passengers = input('Enter passengers: ')
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
    #if os.path.isfile(file):