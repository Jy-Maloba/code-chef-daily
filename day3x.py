# Problem
# Bob has an account in the Bobby Bank. His current account balance is WW rupees.

# Each month, the office in which Bob works deposits a fixed amount of XX rupees to his account.
# YY rupees is deducted from Bob's account each month as bank charges.

# Find his final account balance after ZZ months. Note that the account balance can be negative as well.

# Input Format
# The first line will contain TT, the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing four integers W,X,Y,W,X,Y, and ZZ — the initial amount, the amount deposited per month, the amount deducted per month, and the number of months.
# Output Format
# For each test case, output in a single line the final balance in Bob's account after ZZ months.

# cook your dish here
t = int(input())

for i in range(t):
    (w,x,y,z) =map(int, input().split(" "))
    for n in range(z):
        w = w+x-y
    print(w)