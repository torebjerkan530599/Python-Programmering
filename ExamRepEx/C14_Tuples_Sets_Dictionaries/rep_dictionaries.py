#NB! Difference between creating empty set and dictionary. Curly braces are used for both sets and dictionaries.***

set1 = set() # to create empty set
set2 = {("A","B"),("C",)} # a set of two tuples
set3 = {1,2,3} #NB, only if the set has initial values should curly braces be used***

dict1 = {} # to create empty dictionary
dict2 = dict() # also to create empty dictionary
dict3 = {'A':("Ann","Albert"), 'B':("Bernard","Benny")} # a dict whose keys are characters and values are tuples 
dict3.update({'D': ("Wesley","Snipes")}) #same as appending

d = {"helena":50, "bakary":45, "aiysha":54}
print(len(d))
print(max(d)) # get key that has the max value (alphabetically)
print(d[max(d)]) #access value of the key that has the max value
print(min(d)) #...and visa verca
print(d[min(d)])

'''
another example of finding the key assosiated withe the max value
max_key = max(d.keys())
val_of_max = d[max_key]
'''


''' 
another example of update, 
if state_capitals and provincial_capitals are also dictionaries
regional_capitals = {}
regional_capitals.update(state_capitals)
regional_capitals.update(provincial_capitals)
'''
dict3['B'] = ("Benny","Hill") # change the value mapped to by the key B 

print(f'dict3: {dict3}')
# Accessing dictionaries

# returning value from entry with key "A"
print(dict3['A']) 

# 
# The get(key) method is similar to dictionary_name[key] 
# except that the get method returns None 
# if the key is not in the dictionary rather than raising an exception.

print(dict3.get('C')) # returns None if key doesn't exist
print(len(dict3))

print('B' in dict3)

# returning specific keys
first_key = list(dict3.keys())[0]
second_key = list(dict3.keys())[1]
print("first key: " + first_key + ", second key: " + second_key)

dict4 = {("Peter", "Frampton"):5000, ("Joshua","Tree"): 2000, ("Cal",2): 10000}
first_key_second_value_in_tuple = tuple(dict4.keys())[0][1]
print(first_key_second_value_in_tuple)
last_key_second_value_in_tuple = tuple(dict4.keys())[len(dict4)-1][1]
print(last_key_second_value_in_tuple)

del dict4[("Cal",2)] # use del with keyword to delete an entry
print(dict4)

#del dict4[min(dict4)] # to delete entry with smallest key
dict4.popitem()
print(f'After popitem: {dict4}') # popitem pops the last inserted item lifo (stack)
print(dict4.pop(tuple(dict4.keys())[0])) # to return a value and remove it at the same time use pop

print(dict4)

'''
another example. 
remove all entries in a dictionary d
whose key is an element in a list, lst

for e in lst:
    if e in d:
        del d[e]
'''

# reminder of what is leagal operations and not
d = {1:[1, 2], 3:[3, 4]}  # Correct
#d = {[1, 2]:1, [3, 4]:3}  # Incorrect, key must be immutable
d = {(1, 2):1, (3, 4):3}  # Correct
d = {1:"ashley", 3:"gabriel"} # Correct
d = {"ashley":1, "gabriel":3} # Correct
d = dict([["ashley", 1], ["gabriel", 3]]) # Correct


d2 = {"red":4, "blue":1, "green":14, "yellow":2}
print(d2["red"])
print(list(d.keys()))
print(list(d.values()))
print("blue" in d)
print("purple" in d)
d2["blue"] += 10
print(d2["blue"])

'''
looping dictionaries:
Given a variable, province_premier, 
associated with a dictionary that maps the province
names to the names of province premiers, 
associate with premier_province a dictionary that is
the inverse of province_premier, 
i.e., one that maps names of premiers to province names. 
Your code needs to first create an empty premier_province.

premier_province = {} # the opposite would be province_premier = {}

for province,premier in province_premier.items(): 
    premier_province[premier] = province # reorder elements
'''
'''
max_key = max(d.keys())
val_of_max = d[max_key]
'''

# in and not in operators to determine wether a key is present in a dictionary
students = {"111-34-3434":"Ashley", "132-56-6290":"Gabriel"}
print("111-34-3434" in students)
print("111-34-3434" not in students)
d1 = {"red":41, "blue":3}
d2 = {"blue":3, "red":41}
print(f'student keys: {students.keys()}') # will print dict_keys(['111-34-3434', '132-56-6290'])
print(f'student keys: {tuple(students.keys())}')  # will print ('111-34-3434', '132-56-6290')
print(tuple(students.values()))
print(tuple(students.items()))
students.clear() # to empty the dictionary
# to test if two dictionaries are equal, other comparasion operators are not allowed
print(d1 == d2)
print(d2 != d2)


# reverse the values in a dictionary
inverse = {}
for key,value in d.items():
    inverse[value] = key
    
'''
Given dictionaries, d1 and d2, 
create a new dictionary named d3 with the following property: 
for each entry (a, b) in d1, if there is an entry (b, c) in d2, 
then the entry (a, c) should be added to the new dictionary. 
For example, if d1 is {2:3, 8:19, 6:4, 5:12} and d2 is {2:5, 4:3, 3:9}, the
n the new dictionary should be {2:9, 6:3}.

d3 = {}

for key,value in d1.items():
    if value in d2.keys():
        d3[key] = d2[value]

'''

d3 = {}
d1 = {2:3, 8:19, 6:4, 5:12}
d2 = {2:5, 4:3, 3:9}
for key,value in d1.items():
    if value in d2.keys():
        d3[key] = d2[value]
print(d3)

#Create party_size a dictionary that maps party names to the number of members they have.
'''
# mp_affiliation = {names:party}

party_size = {}

for member,party in mp_affiliation.items():
    if party in party_size:
        party_size[party] += 1
    else:
        party_size[party] = 1
'''