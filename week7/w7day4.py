# Problem
# Chef and Chefina are competing against each other in a programming contest. 
# They were both able to solve all the problems in the contest, so the winner between them must be decided by time penalty. 
# Chef solved all the problems in X minutes and made P wrong submissions, 
# while Chefina solved all the problems in Y minutes and made Q wrong submissions. Who won the competition (or was it a draw)?

# Note: The time penalty is calculated as follows:

# The base time penalty is the time at which the final problem was solved (so, X for Chef and Y for Chefina)
# Each wrong submission adds a penalty of 10 minutes
# The winner is the person with less penalty time. If they both have the same penalty, it is considered a draw.

# cook your dish here
t = int(input())

for i in range(t):
    x,y,p,q= map(int, input().split(' '))
    chef = x+(p*10)
    fina = y +(q*10)
    
    if chef < fina:
        print("Chef")
    elif fina < chef:
        print("Chefina")
    else:
        print("Draw")
    