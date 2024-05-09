# 14.2 solution nr. 1, my solution
lst = [-3, 0, 0, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5]
print ("Original list solution 1 : " + str(lst))
frequency_max = max({lst.count(i) for i in set(lst)})
values = {i for i in set(lst) if lst.count(i) == frequency_max}
print(values)

# Alternative elegant solution
# initializing list
test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]
 
# printing original list
print ("Original list solution 2: " + str(test_list))
 
# using list comprehension to get most frequent element
res = max(set(test_list), key = lambda x: test_list.count(x))
 
# printing result
print ("Most frequent number is : " + str(res))
#this code is contributed by Vinay Pinjala.
