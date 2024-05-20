class Person: 
    def __init__(self, name, children=None): 
        self.name = name
        self.children = children if children is not None else []

def count_offspring(person):
    if not person.children:
        return 0
    total_offspring = len(person.children)
    for child in person.children:
        total_offspring += count_offspring(child)
    return total_offspring

# Creating the family tree
p1 = Person("Eric")
p2 = Person("Ariana")
p3 = Person("Mark", [p1, p2])
p4 = Person("John")
p5 = Person("Mary", [p3, p4])
p6 = Person("Edward")
p7 = Person("Helen", [p5, p6])

# Sample run
print(f"{p7.name} has {count_offspring(p7)} children")
