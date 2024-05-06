student1 = {"gabriel", "ashley", "tim"}
student2 = {"gabriel", "emilia", "tim"}
print(student1.issuperset({"ashley"})) # True
print(student1.issubset(student2)) # False
print({1, 2, 3} > {1, 2, 4}) # False
print({1, 2, 3} < {1, 2, 4}) # False
print({1, 2} < {1, 2, 4}) # True
print({1, 2} <= {1, 2, 4}) # True

s1 = {1, 4, 8 ,3 ,5}
s2 = {1, 3, 5, 10}
s3 = {1, 3 ,5}

print(f"s1 is a subset of s2 {s1 <= s2}")
print(f"s2 is a subset of s1 {s2 <= s1}") 
print(f"s1 is a proper subset of s2 {s1 < s2}") # only < or > without = signifies proper
print(f"s1 is a subset of s3 {s1 <= s3}")
print(f"s1 is proper subset of s3 {s1 < s3}")

# 4 different set-operations

# union 
print(s1 | s2 | s3) # values in all sets 

# intersection
print(s1 & s2 & s3) # all values common among sets

# difference
print(s1 - s2) # all values in s1 not in s2

# symmetric difference (xor)
print(s1 ^ s2) # all values not common among s1 and s2

# set operations can be used on anonymous sets
print({"green", "red", "blue", "red"} ^ {"green", "yellow"})