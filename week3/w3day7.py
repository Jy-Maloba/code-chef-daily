# Problem
# Janmansh and Jay are playing a game. They start with a number XX and they play a total of YY moves. Janmansh plays the first move of the game, after which both the players make moves alternatingly.

# In one move, a player can increment or decrement XX by 11.

# If the final number after performing YY moves is even, then Janmansh wins otherwise, Jay wins. Determine the winner of the game if both the players play optimally.

# Input Format
# The first line will contain TT - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers XX, YY - the starting number and the total number of moves respectively.
# Output Format
# For each test case, output the winning player (Janmansh or Jay).

# cook your dish here
t = int(input())
for i in range(t):
    (x,y)= map(int, input().split(' '))
    a = x+y
    if a %2==0:
        print("Janmansh")
    else:
        print("Jay")