# Chef has two integers XX and YY. Chef wants to perform some operations to make XX and YY equal. In one operation, Chef can either:

# set X := X + 1X:=X+1
# or set Y := Y + 2Y:=Y+2
# Find the minimum number of operations required to make XX and YY equal.

# Input Format
# The first line contains a single integer TT — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two space separated integers XX and YY.
# Output Format
# For each test case, print the minimum number of operations required to make XX and YY equal.

# cook your dish here
t = int(input())

for i in range(t):
    (x,y)= map(int, input().split(' '))
    c = 0
    if x==y: #if they are already equal
        print(c)
    elif x<y: #if x is less
        c=c+(y-x) #y-x to get how many time we'll add 1 to get to y..assign that value to c
        print(c)
    elif x>y: #if y is less
        x=x-y #get their difference
        if x%2==0:#if theri difference is divisible by 2
            c=c+(x//2) #divide it by 2 to get the number of times you'll add 2 to get to x and assign that value to c
            print(c)
        else: #if the difference is not divisible by 2
            c=c+(x//2)+2 #add an extra 2 after dividing
            print(c)