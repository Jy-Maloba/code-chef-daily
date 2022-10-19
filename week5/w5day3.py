# Ash is trying to get visa to Chefland. For the visa to be approved, he needs to satisfy the following three criteria:

# Solve at least x problems on Codechef.
# Have at least y current rating on Codechef.
# Make his last submission at most z months ago.
# You are given the number of problems solved by Chef a his current rating b and the information that he made his last submission months ago. Determine whether he will get the visa c.

# Input
# The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
# The first and only line of each test case contains six space-separated integers a,y,z,a,b,c

# Output
# For each test case, print a single line containing the string "YES" if Chef will get the visa or "NO" if he will not.

# cook your dish here
t= int(input())

for i in range(t):
    (x,a,y,b,z,c) = map(int, input().split(' '))
    if a>=x and b>=y and c<=z:
        print("YES")
    else:
        print("NO")