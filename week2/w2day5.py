# It's the soccer match finals in Chefland and as always it has reached the penalty shotouts. 
# Each team is given 55 shots to make and the team scoring a goal on the maximum number of shots wins the game.
#  If both the teams' scores are equal, then the game is considered a draw and we would have 22 champions.

# Given ten integers A_1, A_2,...A10where the odd indexed integers 
# represent the outcome of the shots made by team 1 and even indexed integers(A_2, A_4, A_6, A_8, A_{10}
# represent the outcome of the shots made by team 2 (here A_i = 1 indicates that it's a goal and A_i = 0 
# indicates a miss), determine the winner or find if the game ends in a draw.

# Input Format
# The first line of input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
# The first and only line of each test case contains ten space-separated integers
# Output Format
# For each test case, print a single line containing one integer - 00 if the game ends in a draw or 11 if the first team wins or 22 if the second team wins.

# cook your dish here
t = int(input())

for i in range(t):
    (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10) = map(int, input().split(' '))
    team1 = a1+a3+a5+a7+a9
    team2 = a2+a4+a6+a8+a10
    if team1 >team2 :
        print(1)
    elif team2>team1:
        print(2)
    else:
        print(0)


# another way of executing it
t = int(input())

for i in range(t):
    team1=0
    team2=0
    shots=list(map(int,input().split()))
    for item in range(0,10,2):
        team2=team2+shots[item]
    for x in range(1,10,2):
        team1=team1+shots[x]
    if team1 >team2 :
        print(2)
    elif team2>team1:
        print(1)
    else:
        print(0)