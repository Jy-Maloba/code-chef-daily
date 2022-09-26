# Problem
# In computing, the collection of four bits is called a nibble.

# Chef defines a program as:

# Good, if it takes exactly XX nibbles of memory, where XX is a positive integer.
# Not Good, otherwise.
# Given a program which takes NN bits of memory, determine whether it is Good or Not Good.

# Input Format
# First line will contain TT, number of test cases. Then the test cases follow.
# The first and only line of each test case contains a single integer NN, the number of bits taken by the program.
# Output Format
# For each test case, output \texttt{Good}Good or \texttt{Not Good}Not Good in a single line.

# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    if n%4==0:
        print("Good")
    else:
        print("Not Good")