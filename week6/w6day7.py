# Problem
# You are given an integer N.
#  Find if it is possible to represent N as the sum of several(possibly zero) 2's 
# and several(possibly zero) 7's.

# Formally, find if there exist two integers X,Y (X,Y≥0) that 
#  such that 2 * X + 7* Y =N.

# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    if (n%2==0) or (n>=7):
        print("YES")
    else:
        print("NO")