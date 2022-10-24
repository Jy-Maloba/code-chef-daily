# Chef prepared a problem. The admin has rated this problem for xx points.

# A problem is called :

# Easy if 1 <= x <100

# Medium if 100<= x <200

# Hard if 200<= x <=300

# Find the category to which Chef’s problem belongs.

# cook your dish here
t = int(input())

for i in range(t):
    x = int(input())
    if x>=1 and x<100:
        print("Easy")
    elif x>=100 and x<200:
        print("Medium")
    elif x >= 200 and x<=300:
        print("Hard")