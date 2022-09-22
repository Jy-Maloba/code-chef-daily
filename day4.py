# Problem
# The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:

# Rent a cooler at the cost of XX coins per month.
# Purchase a cooler for YY coins.
# Given that the summer season will last for MM months in Chefland, help Chef in finding whether he should rent the cooler or not.

# Chef rents the cooler only if the cost of renting the cooler is strictly less than the cost of purchasing it. Otherwise, he purchases the cooler.

# Print \texttt{YES}YES if Chef should rent the cooler, otherwise print \texttt{NO}NO.

# Input Format
# The first line of input will contain an integer TT — the number of test cases. The description of TT test cases follows.
# The first and only line of each test case contains three integers XX, YY and MM, as described in the problem statement.
# Output Format
# For each test case, output \texttt{YES}YES if Chef should rent the cooler, otherwise output \texttt{NO}NO.

# cook your dish here
t = int(input())

for i in range(t):
    (x,y,m)=map(int, input().split(" "))
    if x*m >=y:
        print("NO")
    else:
        print("YES")