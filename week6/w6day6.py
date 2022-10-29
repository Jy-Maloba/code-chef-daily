# Problem
# Chef's professor is planning to give his class a group assignment. 
# There are 2N2N students in the class, with distinct roll numbers ranging from 11 to 2N2N. 
# Chef's roll number is XX.

# The professor decided to create NN groups of 22 students each. 
# The groups were created as follows: the first group consists of roll numbers 11 and 2N2N, 
# the second group of roll numbers 22 and 2N - 12N−1, and so on, with the final group consisting of roll numbers NN and N+1N+1.

# Chef wonders who his partner will be. Can you help Chef by telling him the roll number of his partner?

# cook your dish here
t=int(input())

for i in range(t):
    n,x=map(int, input().split(' '))
    g=2*n
    print(g-x+1)