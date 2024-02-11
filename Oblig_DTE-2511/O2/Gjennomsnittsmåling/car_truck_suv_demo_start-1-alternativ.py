# This program creates a Car object, a Truck object,
# and an SUV object
import os.path
import pickle
import Vehicle
import Speeders

# Constants for the menu choices
class Choice:
    NEW_CAR = 1
    NEW_TRUCK = 2
    NEW_SUV = 3
    FIND_VEHICLE = 4
    SHOW_VEHICLES = 5
    SHOW_TICKETS = 6
    QUIT = 7
    
def main():
    if os.path.isfile('vehicles.dat'):
        with open('vehicles.dat', 'rb') as file:
            vehicle_list = pickle.load(file)    
    else:
        # A collection of vehicles to be written to file initially for testing purposes
        vehicle_list = [Vehicle.Car('BMW 320', 2001, 70000, 15000.0 , 4, 'FY99401'), 
                       Vehicle.Suv('Volvo XC60', '2010', ' 30000' , 18500.0, 5, 'TEST123'), 
                       Vehicle.Truck('Toyota RAV4', 2002, 40000, 12000.0, '4WD', 'TEST234')]
        
        with open('vehicles.dat', 'wb') as picklefile:
            pickle.dump(vehicle_list, picklefile)
            print('vehicles.dat was created in current working directory')
            print('vehciles.dat contains the following vehicles initially: ')
        for vehicle in vehicle_list:
            print(vehicle)
    
    while True:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
            switch(choice, vehicle_list)
        except ValueError:
            print('Invalid type of input. Only numbers accepted. Text or other symbols is not valid')
    
def switch(choice,vehicle_list):

    match choice:
        case Choice.NEW_CAR | Choice.NEW_TRUCK | Choice.NEW_SUV:
            vehicle_list.append(new_vehicle(choice))
            
        case Choice.FIND_VEHICLE:
            name = input('Find vehicle by name: ')
            for vehicle in vehicle_list:
                if vehicle.make.startswith(name):
                    print(vehicle)
                
        case Choice.SHOW_VEHICLES:
            print('The following cars are in inventory:')
            for v in vehicle_list:
                print(v)
        
                    
        case Choice.SHOW_TICKETS:
            speeders_dict = Speeders.listSpeeders('box_a.txt', 'box_b.txt', Speeders.SPEED_LIMIT, Speeders.DISTANCE)
            for vehicle in vehicle_list:
                if vehicle.licence_plate in speeders_dict:
                    ticket = Vehicle.SpeedTicket(vehicle.licence_plate, speeders_dict[vehicle.licence_plate][1], speeders_dict[vehicle.licence_plate][0], Speeders.SPEED_LIMIT)
                    # if ticket not in vehicle.tickets:
                    #      vehicle.tickets = ticket
                    print(ticket)
                
        case Choice.QUIT:
            vehicle_collection_sorted = sorted(vehicle_list, key=lambda vehicle: vehicle.make, reverse=False)
            
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
    licence_plate = input("Enter registration: ")   
    
    if choice == Choice.NEW_CAR:
        doors = input('Enter doors: ')
        return Vehicle.Car(make,model,mileage,price,doors,licence_plate)
    if choice == Choice.NEW_TRUCK:
        drive_type = input('Enter drive type: ')
        return Vehicle.Truck(make,model,mileage,price,drive_type,licence_plate)
    if choice == Choice.NEW_SUV:
        passengers = input('Enter passengers: ')
        return Vehicle.Suv(make,model,mileage,price,passengers,licence_plate)

# The display_menu function displays a menu.
def display_menu():
    print('\n')
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Show speeders')
    print('7) Quit')
    print()

# Call the main function.
if __name__ == '__main__':
      main()