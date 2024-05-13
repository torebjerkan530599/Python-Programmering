class TSD(): #for tuple,set and dictionary
    def __init__(self, values) -> None:
        self.values = values
    def output(self):
        return self.values
    def square(self,value):
        return value**2
    
if __name__ == "__main__":
    #https://youtu.be/twxE0dEp3qQ?si=ZZ0V3V2LLmGUIuEz
    output = [x for x in range(50) if x % 2 == 0]
    print(output)

# format: values = [expression for item in if condition(s)]
# list with squares - comprehension
ex_1 = [x * x for x in range(10) if x%2 == 0]
print(ex_1)
a_dict = {char: chr(char).upper() for char in range(ord('a'),ord('a') + 26)} # format: key: values = expression for item if condition(s)
print(a_dict)

options = ["any","albany","apple","world","hello",""]
output = [word 
         for word in options 
         if not len(word) <= 1 
         if word[0] == "a" 
         if word[-1] == "y"] # if after the loop to make selections from a list, a.k.a filtering a list*
print(output) 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# num is the value in the inner loop we are interested in and hence we place the num furthest to the left for output
flattened = [num for row in matrix for num in row] 
print(flattened)

# if first to the left in the comprehension to build a list on certain criteria, nb: note that output is placed first, nbb: we're not filtering the list*
categories = ["even" if num % 2 == 0  else "odd" for num in range(10)] # inserting values instead of filtering, see line 19
print(categories)

lst = [[num for num in range(5)] for _ in range(5) ] # building a list inside a list, just add on more "for _"- loops with brackets to get more dimensions
print(lst)

# functions inside comprehensions
program = TSD(None)
squared_numbers = [program.square(x) for x in range(10) if program.square(x) < 50] # x itself won't work for filtering numbers
print(squared_numbers)

# Mapping states with their capitals with using dictionary comprehension
pairs = [("a",1), ("b",2), ("c",2)] # a list of tuples
my_dict = {k:v for k,v in pairs} # converting the list of tuples to a dictionary comprehension
print(my_dict)

#removing duplicates from a list while applying a function
nums = [1,2,2,3,3,3,4,4,4,4,4,4]
unique_nums_set = {x ** 2 for x in nums}
print((unique_nums_set))

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
dict_using_comp = {key:value for (key, value) in zip(state, capital)}
   
print("Output Dictionary using dictionary comprehensions:", 
                                           dict_using_comp)


# Generator comprehension 
sum_of_squares = sum(x**2 for x in range(1000000)) # using a generator avoids the need to generate all values in advance, which is heavy on memory
# we don't need to have all values at the same time, we just need them one at a time so that we can add them together. That is what this example portrays.
# A generator only generates values when they need to be used. Doesn't store values in memory. It will give you the next value when you ask for it.
# the range function in this example is going to return values one by one, and not generate an entire list. sum works in such a way that it asks for each value 
# sequentially, and add it to a sume that it's storing internally, so it doesn't need to know what the previous or next square is, it just accesses the current
# square it's looking at and adds it to the sum it's keeping track of. However, adding brackets to the expression, like this: sum([x**2 for x in range(1000000)])
# would generate every single square and store it in a list AND THEN I would pass that list to sum, so DON'T DO THAT!

# that old
def to1D(self,row, col):
        index = row * 3 + col # number of columns is 3
    
    
    
    