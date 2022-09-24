# initializing list  
test_list = [(1, 6), (3, 4), (5, 8)]

# printing original list  
print("The original list is : " + str(test_list))

# position Summation in List of Tuples 
# using list comprehension 
res = sum(i[0] for i in test_list), sum(i[1] for i in test_list)

# printing summation 
print("The position summation of tuples  : " + str(res))