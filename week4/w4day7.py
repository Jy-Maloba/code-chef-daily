# Problem
# Chef is a big fan of Coldplay. Every Sunday, he will drive to a park taking MM minutes to reach there, and during the ride he will play a single song on a loop. Today, he has got the latest song which is in total SS minutes long. He is interested to know how many times will he be able to play the song completely.

# Input
# The first line contains an integer TT - the number of test cases. Then the test cases follow.
# The only line of each test case contains two space-separated integers M, SM,S - the duration of the trip and the duration of the song, both in minutes.
# Output
# For each test case, output in a single line the answer to the problem.

# cook your dish here
t= int(input())
for i in range(t):
    (m,s)=map(int, input().split(' '))
    time=m//s
    print(time)