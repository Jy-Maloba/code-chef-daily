# Problem
# Chef goes to the supermarket to buy some items. Luckily there's a sale going on under which Chef gets the following offer:

# If Chef buys 33 items then he gets the item (out of those 33 items) having the lowest price as free.
# For e.g. if Chef bought 33 items with the cost 66, 22 and 44, then he would get the item with cost 22 as free. So he would only have to pay the cost of the other two items which will be 6 + 4 = 106+4=10.

# Chef buys 33 items having prices AA, BB and CC respectively. What is the amount of money Chef needs to pay?

# Input Format
# The first line will contain an integer TT - number of test cases. Then the test cases follow.
# The first and only line of each test case contains three integers A, B, CA,B,C - the prices of the items bought by Chef.
# Output Format
# For each test case, output the price paid by Chef.

# cook your dish here
#how I did it.. (it works)
t = int(input())

for i in range(t):
    (a, b, c)=map(int, input().split(' '))
    if a<b and a<c:
        print(b+c)
    elif b<a and b<c:
        print(a+c)
    else:
        print(a+b)

#how it "should be done"

T = int(input())
for a in range(T):
    lst = list(map(int,input().split()))
    lst.sort()
    A = min(lst)
    lst.remove(A)
    print(sum(lst))