# Problem
# Recently, Devendra went to Goa with his friends. Devendra is well known for not following a budget.

# He had Rs. Z at the start of the trip and has already spent Rs. Y on the trip. 
# There are three kinds of water sports one can enjoy, with prices Rs. A, B, and C. He wants to try each sport at least once.

# If he can try all of them at least once output YES, otherwise output NO.

# cook your dish here
t = int(input())
for i in range(t):
    z,y,a,b,c = map(int, input().split(' '))
    m =y+a+b+c
    if z>=m:
        print("YES")
    else:
        print("NO")
    