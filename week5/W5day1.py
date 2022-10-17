# Problem
# Vacations have arrived and Chef wants to go to his home in ChefLand. There are two types of routes he can take:

# Take a flight from his college to ChefArina which takes XX minutes and then take a bus from ChefArina to ChefLand which takes YY minutes.
# Take a direct train from his college to ChefLand which takes ZZ minutes.
# Which of these two options is faster?

# Input Format
# The first line of the input contains a single integer TT - the number of test cases. The test cases then follow.
# The first line of the test case contains three space-separated integers XX, YY, and ZZ.
# Output Format
# For each test case, if Chef takes the train output TRAIN, if Chef takes the plane and the bus output PLANEBUS, if both are equal output EQUAL.

# cook your dish here
t= int(input())
for i in range(t):
    (x,y,z)=map(int, input().split(' '))
    flight = x+y
    train = z
    
    if flight < train:
        print("PLANEBUS")
    elif train<flight:
        print("TRAIN")
    elif flight == train:
        print("EQUAL")