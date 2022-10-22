# Problem
# Chef is planning to buy a new car for his birthday. After a long search, he is left with 22 choices:

# Car 1: Runs on diesel with a fuel economy of xa km/l
# Car 2: Runs on petrol with a fuel economy of xb km/l
# Chef also knows that the current price of diesel is ya rupees per litre
# the current price of petrol is yb rupees per litre
# Assuming that both cars cost the same and that the price of fuel remains constant, which car will minimize Chef's expenses?

# Print your answer as a single integer in the following format

# If it is better to choose Car 1, print -1−1
# If both the cars will result in the same expenses, print 00
# If it is better to choose Car 2, print 11

t = int(input())

for i in range(t):
    (xa,xb,ya,yb)= map(int, input().split(' '))
    car1 = ya/xa
    car2 = yb/xb
    if car1<car2:
        print(-1)
    elif car2==car1:
        print(0)
    else:
        print(1)