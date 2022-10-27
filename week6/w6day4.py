# Problem
# In Uttu's college, a semester is said to be a:

# Overload semester if the number of credits taken \gt 65>65.
# Underload semester if the number of credits taken \lt 35<35.
# Normal semester otherwise
# Given the number of credits XX taken by Uttu, determine whether the semester is Overload, Underload or Normal.

# Input Format
# The first line will contain TT - the number of test cases. Then the test cases follow.
# The first and only of each test case contains a single integer XX - the number of credits taken by Uttu.

# Output Format
# For each test case, output Overload, Underload or Normal depending upon the number of credits taken by Uttu.

# cook your dish here
t = int(input())

for i in range(t):
    x= int(input())
    if x > 65:
        print("Overload")
    elif x < 35:
        print("Underload")
    else:
        print("Normal")