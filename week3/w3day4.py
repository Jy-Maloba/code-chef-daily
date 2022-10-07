# Problem
# Alice, Bob and Charlie are bidding for an artifact at an auction.
# Alice bids AA rupees, Bob bids BB rupees, and Charlie bids CC rupees (where AA, BB, and CC are distinct).

# According to the rules of the auction, the person who bids the highest amount will win the auction.
# Determine who will win the auction.

# Input Format
# The first line contains a single integer TT — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains three integers AA, BB, and CC, — the amount bid by Alice, Bob, and Charlie respectively.
# Output Format
# For each test case, output who (out of Alice, Bob, and Charlie) will win the auction

# cook your dish here
t = int(input())

for i in range(t):
    (a, b, c) = map(int, input().split(' '))
    if a > b and a> c:
        print("Alice")
    elif b>a and b>c:
        print("Bob")
    else:
        print("Charlie")