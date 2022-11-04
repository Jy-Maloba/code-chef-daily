# Problem
# Suppose Chef is stuck on an island and currently he has x units of food supply and y units of water supply in total
# that he could collect from the island. He needs m units of food supply and n  units of water supply per day at the minimal
#  to have sufficient energy to build a boat from the woods and also to live for another day. 
# Assuming it takes exactly D days to build the boat and reach the shore, 
# tell whether Chef has the sufficient amount of supplies to be able to reach the shore by building the boat?

# ###Input:

# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains of a single line of input, five integers x, y, m,n,D

# cook your dish here
t = int(input())

for i in range(t):
    x,y,m,n,d = map(float, input().split(' '))
    food_days = x/m
    water_days = y/n
    
    days = min(food_days,water_days)
    
    if days >= d:
        print("YES")
    else:
        print("NO")
        