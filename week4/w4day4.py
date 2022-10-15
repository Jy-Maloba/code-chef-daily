# Problem
# Chef has two numbers AA and BB.

# In one operation, Chef can choose either AA or BB and multiply it by 22.

# Determine whether he can make both AA and BB equal after any number (possibly, zero) of moves.

# Input Format
# The first line of input will contain a single integer TT, denoting the number of test cases.
# Each test case consists of two space-separated integers AA and BB.
# Output Format
# For each test case, output YES if Chef can make both numbers equal, NO otherwise.

# cook your dish here
t = int(input())

for i in range(t):
    (a, b) = map(int, input().split(' '))
    if a==b:
        print("YES")
    elif a<b:
        while a<b:
            a*=2 
        if a==b:
            print("YES")
        else:
            print("NO")
    elif b<a:
        while b<a:
            b*=2 
        if a==b:
            print("YES")
        else:
            print("NO")