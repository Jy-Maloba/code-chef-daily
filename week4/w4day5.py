# Chefland has 22 different types of coconut, type A and type B. Type A contains only x milliliters of coconut water and type B contains only y 
# grams of coconut pulp. Chef's nutritionist has advised him to consume a milliliters of coconut water and b grams of coconut pulp every week in the summer. 
# Find the total number of coconuts (type AA + type BB) that Chef should buy each week to keep himself active in the hot weather.

# Input
# The first line contains an integer TT, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, four integers

# Output
# For each test case, output in a single line the answer to the problem.

# cook your dish here
t = int(input())

for i in range(t):
    (x,y,a,b) = map(int, input().split(' '))
    m =a//x #number of type A coconuts
    n = b//y #number of type BB coconuts
    total = m+n
    print(total)