# Problem
# While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000.
# If the quantity and price per item are input, write a program to calculate the total expenses.

# cook your dish here
t = int(input())
for i in range(t):
    (q,p)=map(int, input().split(' '))
    total = q*p
    if total > 1000:
        total = 0.01 * total
        print(total)
    else:
        print(total)