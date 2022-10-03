# Problem
# Chef is currently facing the north direction. Each second he rotates exactly 9090 degrees in clockwise direction. Find the direction in which Chef is facing after exactly XX seconds.

#Note: There are only 4 directions: North, East, South, West (in clockwise order).

# Input Format
# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains of a single integer X.
# Output Format
# For each testcase, output the direction in which Chef is facing after exactly X seconds.

# cook your dish here
t = int(input())

for i in range(t):
    x = int(input())
    s=x%4
    if s==1:
        print("East")
    elif s==2:
        print("South")
    elif s==3:
        print("West")
    elif s==0:
        print("North")