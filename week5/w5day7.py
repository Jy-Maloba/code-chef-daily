# Chef has 2 numbers A and B (A<B).

# Chef will perform some operations on AA.

# In the i^th operation:
# Chef will add 1 to A if i is odd.
# Chef will add 2 to A if i is even.
# Chef can stop at any instant. Can Chef make A equal to B?

# cook your dish here
t = int(input())

for i in range(t):
    (a,b)=map(int, input().split(' '))
    if((b-a)%3==1 or (b-a)%3==0):
        print("YES")
    else:
        print("NO")


# Sample 
# Input
# 4 test cases
# 1 2
# 3 6
# 4 9
# 10 20

# Output
# YES
# YES
# NO
# YES


# Explanation:
# Test case 1: Chef may perform one operation to make A equal to B: 1 --+1-->2

# Test case 2: 3--+1-->4---+2-->6

# Test case 3: It can be shown that it is impossible to make A and B equal.

# Test case 4: 10--+1-->11--+2-->13--+1-->14--+2-->16--+1-->17--+2-->19--+1-->20