# Professor just mentioned two things before vanishing-

# B - separation between left side (LS) and right side (RS) on the ground
# LS - the length of left side
# What should be the length of RS? At one extreme LS can be vertical and at other RS can be vertical. 
# Ron is angry and confused. Since Harry is busy battling Voldemort, its your duty to help him find the minimum and maximum length of RS.

# Input
# First line contains single integer T, the number of test cases. Then T lines follow each containing 2 integers - B and LS.

# Output
# Output T lines, each containing minimum value of RS and maximum value of RS, separated by space. 
# The answer (RS) will be considered correct if it has relative and absolute error less than 10-2.

# cook your dish here
t = int(input())

for i in range(t):
    (b, ls)= map(int, input().split(' '))
    max_rs = b**2 + ls**2 #when rs is the hypotenuse
    min_rs = abs(ls**2-b**2) #when rs is the height
    print(min_rs **0.5, max_rs ** 0.5)