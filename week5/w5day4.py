# Problem
# Write a program to obtain length (L) and breadth (B) of a rectangle 
# and check whether its area is greater or perimeter is greater or both are equal. 

###Input:
# First line will contain the length (L) of the rectangle.
# Second line will contain the breadth (B) of the rectangle.

###Output: Output 2 lines.
# In the first line print "Area" if area is greater otherwise print "Peri" and if they are equal print "Eq".(Without quotes).
# In the second line print the calculated area or perimeter (whichever is greater or anyone if it is equal).

# cook your dish here
l = int(input())
b = int(input())

p = 2 *(l+b)
a = l*b

if a > b:
    print("Area")
    print(a)
elif b>a:
    print("Peri")
    print(b)
else:
    print("Eq")
    print(b)