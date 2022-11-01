# In Chefland, the speed of light is c m/s, and acceleration due to gravity is g m/s 
# Find the smallest height (in meters) from which Chef should jump such that during his journey down,
# only under the effect of gravity and independent of any air resistance, 
# he achieves the speed of light and verifies Einstein's theory of special relativity.

# Assume he jumps at zero velocity and at any time, his velocity (v) and depth of descent (H) are related as v squared=2⋅g⋅H.

# Input
# The first line contains an integer T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, two integers g, c.

# cook your dish here
t= int(input())

for i in range(t):
    g,c=map(int, input().split(' '))
    m = c*c
    n = 2*g
    h=m//n
    print(h)
    