# Given two lists:
# aList = [87, 76, 82, 90, 65]
# bList = [83, 87, 72, 68, 91]
# A) Find the union
# B) Find the intersection
# C) Find the Difference
# D) How many unique values are there?
# Steven Sousa - Quick Quiz - 11/19/2020

aList = [87, 76, 82, 90, 65]
bList = [83, 87, 72, 68, 91]

aSet = set(aList)       # Convert aList into a set
bSet = set(bList)       # Convert bList into a set
print(aSet)
print(bSet)

# A) Find the Union
print("Union of both sets:", aSet | bSet)       # Create union of aSet with bSet

# B) Find the intersection
print("Intersection of sets:", aSet.intersection(bSet))     # Create intersection of aSet with bSet

# C) Find the difference
print("Difference in aSet:", aSet.difference(bSet))              # Find difference between sets using aSet as basis
print("difference in bSet:", bSet.difference(aSet))              # Find difference between sets using bSet as basis

# D) How many unique values are there?
print("Number of unique values:", len(aSet | bSet))         # Union function removes repeated values. Just use len()
