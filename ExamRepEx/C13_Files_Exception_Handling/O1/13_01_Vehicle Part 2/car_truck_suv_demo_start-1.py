# This program creates a Car object, a Truck object,
# and an SUV object.
import Vehicle
import os.path
import pickle

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():
    # Create empty list for vehicles
    vehicles_list = []
    
    # if file exists
    if os.path.isfile('vehicles.dat'):
        with open('vehicles.dat', 'rb') as file:
            vehicles_list = pickle.load(file)
            print('vehciles.dat contains the following vehicles initially:')
        for vehicle in vehicles_list:
            print(vehicle)
        print()
    else:
        print('No vehicles stored yet\n')

    choice = 0
    
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Invalid type of input. Only numbers accepted. Text or other symbols is not valid')
        # Perform the selected action.
        
        if choice == NEW_CAR_CHOICE or  choice == NEW_TRUCK_CHOICE or choice == NEW_SUV_CHOICE:
            vehicles_list.append(new_vehicle(choice))
        elif choice == FIND_VEHICLE_CHOICE:
            name = input('Find vehicle by name: ')
            for vehicle in vehicles_list:
                if str(vehicle._make).startswith(name):
                    print(vehicle)
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            for v in vehicles_list:
                print(v)
        elif choice == QUIT_CHOICE:
            vehicle_collection_sorted = sorted(vehicles_list, key=lambda vehicle: vehicle._make, reverse=False)
            
            #skriv
            with open('vehicles.dat','wb') as file:
                pickle.dump(vehicle_collection_sorted,file)
            
            # les
            print('Vehicles sorted and written to file: ')
            with open('vehicles.dat', 'rb') as file:
                vehciles = pickle.load(file)
            
                for v in vehciles:
                    print(v)
                    
            exit('Exiting the program...')
        else:  
            print('Error: invalid selection. Only 1-6 is valid')   

def new_vehicle(choice):
    make = input('Enter make: ')
    model = input('Enter model: ')    
    mileage = input('Enter milage: ')
    price = input('Enter price: ')
    
    if choice == NEW_CAR_CHOICE:
        doors = input('Enter doors: ')
        return Vehicle.Car(make,model,mileage,price,doors)
    if choice == NEW_TRUCK_CHOICE:
        drive_type = input('Enter drive type: ')
        return Vehicle.Truck(make,model,mileage,price,drive_type)
    if choice == NEW_SUV_CHOICE:
        passengers = input('Enter passengers: ')
        return Vehicle.Suv(make,model,mileage,price,passengers)

# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')



# Call the main function.
if __name__ == '__main__':
      main()