from pathlib import Path
import time
from datetime import datetime
import pickle

SPEED_LIMIT = 60
DISTANCE = 5

def fileToDictionary(txt_file) -> dict:
    vehicles_dict = {}
    try:
        path = Path(__file__).parent / txt_file # reading from the text file in the directory code is run from
        content = path.read_text(encoding="utf-8")
        vehicles_list = [line for line in content.splitlines()]
        #[print(line) for line in vehicles_list]
        # for line in vehicles_list:
        #     key, value = line.strip().split(', ')
        #     vehicles_dict[key] = value
        return {key: value for line in vehicles_list for key, value in [line.strip().split(', ')]}
        #print(vehicles_dict)
    except FileNotFoundError:
        print('file not found')

def listSpeeders(filename_a, filename_b, speed_limit, distance):
    a_dict = fileToDictionary(filename_a)
    b_dict = fileToDictionary(filename_b)
    test_passing_a = a_dict['NB72826']
    test_passing_b = b_dict['NB72826']
    
    
    print(f'first passing at: {test_passing_a}, second passing at: {test_passing_b} ')
    
    # calculate speed
    #for key,key in a_dict,b_dict:
           
    

    

if __name__ == "__main__":

    
    listSpeeders('box_a.txt','box_b.txt', SPEED_LIMIT, DISTANCE)
    