# Problem
# Given an Integer N, write a program to reverse it.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, display the reverse of the given number N, in a new line.

t = int(input())
for i in range(t):
    reverse = 0
    num = int(input())
    while(num):
        remainder = num%10
        reverse =reverse*10+remainder
        num = int(num/10)
    print(reverse)