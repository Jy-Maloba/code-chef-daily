# There is a circular track of length M consisting of M checkpoints and M bidirectional roads such that each road has a length of 11 unit.
# Chef is currently at checkpoint AA and wants to reach checkpoint BB. Find the minimum length of the road he needs to travel.

# cook your dish here
t = int(input())

for i in  range(t):
    (a, b, m) = map(int, input().split(' '))
    x = abs(a-b) # first alternative move directly ahead from A to B
    y = m-x  # second alternative Go back round through M
    print(min(x,y))