# Vasya likes the number 239239. Therefore, he considers a number pretty if its last digit is 22, 33 or 99.

# Vasya wants to watch the numbers between LL and RR (both inclusive), so he asked you to determine how many pretty numbers are in this range. Can you help him?

# Input
# The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
# The first and only line of each test case contains two space-separated integers LL and RR.
# Output
# For each test case, print a single line containing one integer — the number of pretty numbers between LL and RR.

# cook your dish here

t = int(input())

for i in range(t):
    (l,r) = map(int, input().split(' '))
    
    for j in range(l,r+1):
        n = str(j)
        # print(n[::-1])
        c = 0
        
        if n[::-1] == 2 or n[::-1] == 3 or n[::-1] == 9: #this part doesn't execute the way it should
            c= c+1
    print(c)

# another approach
t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        a=i%10
        if a==2 or a==3 or a==9:
            c+=1
    print(c)
        