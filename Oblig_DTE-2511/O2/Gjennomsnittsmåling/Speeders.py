from pathlib import Path
from datetime import datetime
import pickle

def fileToDictionary(txt_file) -> dict:
    try:
        path = Path(__file__).parent / txt_file # reading from the text file in the directory code is run from
        content = path.read_text(encoding="utf-8")
        # content = open(txt_file).read().split("\n")
        #vehicles_list = [line for line in content.splitlines()]
        #[print(line) for line in vehicles_list]
        # for line in vehicles_list:
        #     key, value = line.strip().split(', ')
        #     vehicles_dict[key] = value
        return {key: value for line in content.splitlines() for key, value in [line.strip().split(', ')]}

        #print(vehicles_dict)
    except FileNotFoundError:
        print('file not found')


SPEED_LIMIT = 60
DISTANCE = 5000 # meters
MARGIN_OF_ERROR = 0.05

def listSpeeders(filename_a, filename_b, speed_limit, distance):
    
    speed_with_margin = speed_limit + (speed_limit * MARGIN_OF_ERROR)
    
    dict_speeders = {} # speeders dictionary: {licence_plate: (average_speed, date)}
    
    a_dict = fileToDictionary(filename_a)
    b_dict = fileToDictionary(filename_b)
    
    for licence_plate in a_dict:
        if licence_plate in b_dict: # check if the car reached box_b
            datetime_object_a = datetime.strptime(a_dict[licence_plate], '%Y-%m-%d %H:%M:%S') #string to datetime object
            datetime_object_b = datetime.strptime(b_dict[licence_plate], '%Y-%m-%d %H:%M:%S')
            duration = datetime_object_b - datetime_object_a
            speed = (distance / duration.total_seconds()) * 3.6 # m/s to km/h
            if(speed > speed_with_margin):
                # print(f'{licence_plate} : {speed:.3f} km/h')
                dict_speeders[licence_plate] = (float(format(speed, ".3f")),a_dict[licence_plate])
                
    #print(f'speeders: {dict_speeders}')
    return dict_speeders    
if __name__ == "__main__":
    lawbreakers = listSpeeders('box_a.txt','box_b.txt', SPEED_LIMIT, DISTANCE)
    