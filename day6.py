# Problem
# The weather report of Chefland is Good if the number of sunny days in a week is strictly greater than the number of rainy days.

# Given 7 integers A_1, A_2, A_3, A_4, A_5, A_6, A_7 where A_i = 1 denotes that the i^{th} day of week in Chefland is a sunny day,
# A_i = 0 denotes that the i^{th} day in Chefland is a rainy day. Determine if the weather report of Chefland is Good or not.

# Input Format
# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains of a single line of input, 7 space separated integers A_1, A_2, A_3, A_4, A_5, A_6, A_7A 

# Output Format
# For each testcase, print "YES" if the weather report of Chefland is Good, otherwise print "NO".

# cook your dish here
t= int(input())
for i in range(t):
    sunny,rainy = 0,0
    (a1,a2,a3,a4,a5,a6,a7) = map(int, input().split(' '))
    days = [a1,a2,a3,a4,a5,a6,a7]
    for i in days:
        if i ==1:
            sunny += 1
        else:
            rainy += 1
    if sunny > rainy:
        print("YES")
    else:
        print("NO")


#Another way of doing it...
# n=int(input())
# for i in range(n):
#     c,z=0,0
#     l=[int(i) for i in input().split()]
#     for i in range(len(l)):
#         if l[i]==1:
#             c+=1
#         else:
#             z+=1
#     if c>z:
#         print("YES")
#     else:
#         print("NO")
