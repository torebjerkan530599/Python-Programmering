# d = {(1, 2):1, (3, 4):3}  # Correct
# print(d[3,4])

# students = {"ashley":3, "gabriel":2, "helena":3}
# print(students)
# del students["gabriel"]
# print(students)
d = {5:3, 4:1, 12:2}
max_key = max(d.keys())
val_of_max = d[max_key]

print("Dictionary:", d)
print("Largest key:", max_key)
print("Corresponding value of the largest key:", val_of_max)