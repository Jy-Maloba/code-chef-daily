# Problem
# Chef has a binary string SS of length NN. Chef can perform the following operation on SS:

# Insert any character (00 or 11) at any position in SS.
# Find the minimum number of operations Chef needs to perform so that no two consecutive characters are same in SS.

# Input Format
# The first line contains a single integer TT — the number of test cases. Then the test cases follow.
# The first line of each test case contains an integer NN — the length of the binary string SS.
# The second line of each test case contains a binary string SS of length NN containing 00s and 11s only.
# Output Format
# For each test case, output on a new line the minimum number of operations Chef needs to perform so that no two consecutive characters are same in SS.

# cook your dish here
t= int(input())

for i in range(t):
    length = int(input())
    string = input()

    flag = True
    count = 0
    

    for x in range(length):
     if x+1<length:    
        if string[x] == string[x+1]:
            count += 1
    print(count)