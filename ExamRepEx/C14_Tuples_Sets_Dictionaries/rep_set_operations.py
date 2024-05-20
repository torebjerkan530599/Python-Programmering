# NB:Order is not managed or maintained in sets!!
# set operator precedence: -(difference) &(intersection) ^(xor) |(union)
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
print(f"s1 is equal to s2 is {s1 == s2}")
print(f"s1 is not equal to s2 is {s1 != s2}")
# 4 different set-operations

# union 
print(s1 | s2 | s3) # values in all sets,same as (s1.union(s2)).union(s3)

# intersection
print(s1 & s2 & s3) # all values common among sets, same as (s1.intersection(s2)).intersection(s3)

# difference
print(s1 - s2) # all values in s1 not in s2, same as s1.difference(s2)

# symmetric difference (xor)
print(s1 ^ s2) # all values not common among s1 and s2, same as s1.symmetric_difference(s2)

# set operations can be used on anonymous sets
print({"green", "red", "blue", "red"} ^ {"green", "yellow"})

# sets applied demo
summerMonths = {"Jun", "Jul", "Aug"}
fallMonths = set(("Sep","Oct","Nov")) #NB call to function without curlybraces
winterMonths = set()
winterMonths.add("Dec")
winterMonths.add("Jan")
winterMonths.add("Feb")
springMonths = {"Mar","Apr","May"}
springMonths.add("May") # won't do anything
springMonths.remove("May")
print(springMonths)
springMonths.add("May")
print(springMonths)
summerMonths.add("Sep")
fallMonths.add("Dec")
winterMonths.add("Mar")
springMonths.add("Jun")
startFall = fallMonths.intersection(summerMonths)
print(startFall)
changeMonths = fallMonths.intersection(summerMonths)
changeMonths.union(fallMonths.intersection(winterMonths))
print(changeMonths) # not captured yet, must be assigned
changeMonths = changeMonths.union(fallMonths.intersection(winterMonths))
print(changeMonths) # captured
changeMonths = changeMonths.union(winterMonths.intersection(springMonths))
changeMonths = changeMonths.union(springMonths.intersection(summerMonths))
print(changeMonths) # captured all overlapping months between seasons
yearMonths = (summerMonths.union(fallMonths)).union \
    (winterMonths.union(springMonths))
print(yearMonths)

yearMonths.discard("Dec")
print(yearMonths)
yearMonths.discard("Christmas") #No error thrown
#yearMonths.remove("Christmas") #throws an eror


#programming quiz 14.5
# Given a set weights and an integer desired_weight, 
# remove the element of the set that is closest to desired_weight 
# (the closest element can be less than, equal to or greater than desired_weight), 
# and associate it with the variable actual_weight. 
# For example, if weights is (12, 19, 6, 14, 22, 7) and desired_weight is 18, 
# then the resulting set would be (12, 6, 14, 22, 7) and actual_weight would be 19. 
# If there is a tie, the element less than desired_weight is to be chosen. 
# Thus if the set is (2, 4, 6, 8, 10) and desired_weight is 7, 
# the value chosen would be 6, not 8. Assume there is at least one value in the set

actual_weight = None
min_difference = float('inf')
desired_weight = 18
weights = {12, 19, 6, 14, 22, 7}
desired_weight = 7
weights = {2, 4, 6, 8, 10} 

for weight in weights:
    difference = abs(weight - desired_weight)
    if difference < min_difference or (difference == min_difference and weight < actual_weight):
        actual_weight = weight
        min_difference = difference
weights.remove(actual_weight)

print(weights)