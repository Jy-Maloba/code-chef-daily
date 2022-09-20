# Problem Statement
# Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

# Input
# First line contains the number of triples, N.
# The next N lines which follow each have three space separated integers.
# Output
# For each of the N triples, output one new line which contains the second-maximum integer among the three.

# cook your dish here
n = int(input())

for i in range(n):
    (a,b,c)=map(int, input().split(' '))
    if (a<b and b<c and a<c)or (c<a and b<a and c<b):
        print(b)
    elif (b<a and a<c and b<c) or (c<b and a<b and c<a):
        print(a)
    else:
        print(c)
        #or...
        #elif (a<c and c<b and a<b) or (b<a and c<a and b<c):
        #print(c)
