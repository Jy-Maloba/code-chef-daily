# Problem
# Chef has decided to go to a gold mine along with N of his friends (thus, total N+1N+1 people including Chef go to the gold mine).

# The gold mine contains a total of X kg of gold. Every person has the capacity of carrying up atmost Y kg of gold.

# Will Chef and his friends together be able to carry up all the gold from the gold mine assuming that they can go to the mine exactly once.

# cook your dish here
t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    a=(n+1)*y
    if a>=x:
        print("yes")
    else:
        print("no")