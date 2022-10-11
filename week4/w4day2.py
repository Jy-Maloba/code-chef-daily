# Problem
# There are 33 problems in a contest namely A, B, C respectively. 
# Alice bets Bob that problem CC is the hardest while Bob says that problem BB will be the hardest.
# You are given three integers S_A, S_B, S_CS which denotes the number of successful submissions of the problems A, B, C respectively. 
# It is guaranteed that each problem has a different number of submissions. Determine who wins the bet.
# If Alice wins the bet (i.e. problem CC is the hardest), then output AliceAlice.
# If Bob wins the bet (i.e. problem BB is the hardest), then output BobBob.
# If no one wins the bet (i.e. problem AA is the hardest), then output DrawDraw.
# Note: The hardest problem is the problem with the least number of successful submissions.

# Input Format
# The first line of input contains a single integer TT denoting the number of test cases. 
# The description of TT test cases follows.
# The first and only line of each test case contains three space-separated integers S_A, S_B, S_CS 
# denoting the number of successful submissions of problems A, B, CA,B,C respectively.

# Output Format
# For each test case, output the winner of the bet or print Draw in case no one wins the bet.

# cook your dish here
t = int(input())
for i in range(t):
    (a, b, c) = map(int, input().split(' '))
    if a<b and a<c:
        print("Draw")
    elif b<a and b<c:
        print("Bob")
    else:
        print("Alice")
    