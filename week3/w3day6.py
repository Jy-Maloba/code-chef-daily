# For encoding an even-length binary string into a sequence of A, T, C, and G, we iterate from left to right and replace the characters as follows:

# 00 is replaced with A
# 01 is replaced with T
# 10 is replaced with C
# 11 is replaced with G
# Given a binary string SS of length NN (NN is even), find the encoded sequence.

# Input Format
# First line will contain TT, number of test cases. Then the test cases follow.
# Each test case contains two lines of input.
# First line contains a single integer NN, the length of the sequence.
# Second line contains binary string SS of length NN.
# Output Format
# For each test case, output in a single line the encoded sequence.

# cook your dish here
t = int(input())

for i in range(t):
    s=int(input())
    x=list(input())
    for j in range(0,s,2):
        if(x[j]=="0" and x[j+1]=="0"):
            print("A",end="")
        elif(x[j]=="0" and x[j+1]=="1"):
            print("T",end="")
        elif(x[j]=="1" and x[j+1]=="0"):
             print("C",end="")
        else:
             print("G",end="")
    print() # works as \n for some reason :)