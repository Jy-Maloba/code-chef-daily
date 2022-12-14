# Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

# Minimum age limit is XX (i.e. Age should be greater than or equal to XX).
# Age should be strictly less than YY.
# Chef's current Age is AA. Find whether he is currently eligible to take the exam or not.

# Input Format
# First line will contain TT, number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing three integers X, Y,X,Y, and AA as mentioned in the statement.
# Output Format
# For each test case, output YES if Chef is eligible to give the exam, NO otherwise.

# You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

# cook your dish here
T = int(input())

for i in range(T):
    (X, Y, A) = map(int, input().split(' '))
    if A >= X and A < Y:
        print("YES")
    else:
        print("NO")