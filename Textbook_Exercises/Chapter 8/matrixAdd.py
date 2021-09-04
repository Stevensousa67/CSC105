# Adding matrix together.
# So if you have a set of x and y values
# Note: x and y need to have the same number of rows and columns.

X = [[1,2,3], 
	[4 ,5,6], 
	[7 ,8,9]] 

Y = [[9,8,7], 
	[6,5,4], 
	[3,2,1]] 

#You need a place to put the result values for 'blank' image
result = [[0,0,0], 
	    [0,0,0], 
	    [0,0,0]] 

# iterate through rows 
for i in range(len(X)): 
# iterate through columns 
	for j in range(len(X[0])): 
		result[i][j] = X[i][j] + Y[i][j] 

for r in result: 
	print(r) 
