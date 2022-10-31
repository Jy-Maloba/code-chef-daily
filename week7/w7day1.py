# Problem
# Given the rating RR of a person, tell which division he belongs to. 
# The rating range for each division are given below:

# Division 1: 2000 ≤ Rating.

# Division 2: 1600 ≤ Rating <2000.

# Division 3: Rating <1600.

# cook your dish here
t= int(input())

for i in range(t):
    r=int(input())
    
    if r<1600:
        print(3)
    elif 1600 <= r<2000:
        print(2)
    else: 
        print(1)