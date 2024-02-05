# This program creates a Car object, a Truck object,
# and an SUV object
import os.path
import pickle
import Vehicle

# Constants for the menu choices
class Choice:
    NEW_CAR = 1
    NEW_TRUCK = 2
    NEW_SUV = 3
    FIND_VEHICLE = 4
    SHOW_VEHICLES = 5
    QUIT = 6
    
def main():
    # A collection of vehicles to be written to file initially for testing purposes
    vehicles_list = [Vehicle.Car('BMW 320', 2001, 70000, 15000.0 , 4), 
                       Vehicle.Suv('Volvo XC60', '2010', ' 30000' , 18500.0, 5), 
                       Vehicle.Truck('Toyota RAV4', 2002, 40000, 12000.0, '4WD')]
    
    if os.path.isfile('vehicles.dat'):
        with open('vehicles.dat', 'rb') as file:
            vehicles_list = pickle.load(file)    
    else:
        with open('vehicles.dat', 'wb') as picklefile:
            pickle.dump(vehicles_list, picklefile)
            print('vehicles.dat was created in current working directory')
            print('vehciles.dat contains the following vehicles initially: ')
        for vehicle in vehicles_list:
            print(vehicle)
    
    while True:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
            switch(choice, vehicles_list)
        except ValueError:
            print('Invalid type of input. Only numbers accepted. Text or other symbols is not valid')
    
def switch(choice,vehicles_list):

    match choice:
        case Choice.NEW_CAR | Choice.NEW_TRUCK | Choice.NEW_SUV:
            vehicles_list.append(new_vehicle(choice))
            
        case Choice.FIND_VEHICLE:
            name = input('Find vehicle by name: ')
            for vehicle in vehicles_list:
                if str(vehicle._make).startswith(name):
                    print(vehicle)
                
        case Choice.SHOW_VEHICLES:
            print('The following cars are in inventory:')
            for v in vehicles_list:
                print(v)
                
        case Choice.QUIT:
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
        case _:  
            print('Error: invalid selection. Only 1-6 is valid') 

def new_vehicle(choice):
    make = input('Enter make: ')
    model = input('Enter model: ')    
    mileage = input('Enter milage: ')
    price = input('Enter price: ')
    
    if choice == Choice.NEW_CAR:
        doors = input('Enter doors: ')
        return Vehicle.Car(make,model,mileage,price,doors)
    if choice == Choice.NEW_TRUCK:
        drive_type = input('Enter drive type: ')
        return Vehicle.Truck(make,model,mileage,price,drive_type)
    if choice == Choice.NEW_SUV:
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