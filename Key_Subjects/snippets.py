# Theme: Path and text-files
# from pathlib import Path
# import pickle

# try:
#     path = Path(__file__).parent / "vehicles.txt" # reading from a text file in the directory code is run from
#     content = path.read_text(encoding="utf-8")
# except FileNotFoundError:
#     print('file not found')
    

# Theme: pickle with binary, read only first entry
# name = input('Find vehicle by name: ')
# with open('vehicles.dat', 'rb') as file:
#     objects = pickle.load(file)    
#     for vehicle in objects:
#         if str(vehicle._make).startswith(name):
#             print(vehicle)

# Theme: Dictionary

''' 
Assignment text:
Assume there is a variable, mp_affiliation, associated with a dictionary that maps the names of parliament members to party affiliations. 
Create party_size a dictionary that maps party names to the number of members they have.
'''


mp_affiliation = {
    'John Doe': 'Republican',
    'Jane Smith': 'Democrat',
    'Bob Johnson': 'Republican',
    'Alice Williams': 'Democrat',
    'Charlie Brown': 'Independent',
    'Emily Davis': 'Republican'
}

party_size = {}

for member,party in mp_affiliation.items():
    if party in party_size:
        party_size[party] += 1
    else:
        party_size[party] = 1

#reverse the pairs in a dictionary...
pairs = list(party_size.items())      
items = [[count, word] for (word, count) in pairs] #... using comprehension
print(items)


# You can create the dictionary dict1 by using the zip function to pair elements from list1 and list2
'''his code uses the zip function to pair corresponding elements from list1 and list2, and then the dict constructor is used to convert those pairs into a dictionary. The resulting dict1 will map each element of list1 to its corresponding element in list2.'''
list1 = ['apple', 'banana', 'orange', 'grape']
list2 = [3, 6, 2, 8]

dict1 = dict(zip(list1, list2))

# Print the result
print("List 1:", list1)
print("List 2:", list2)
print("Resulting dictionary dict1:", dict1)


#Create a dictionary named squares that maps the first n counting numbers to their squares.
n = 10
squares = {i: i**2 for i in range(1, n+1)}