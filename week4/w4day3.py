# Chef has three socks in his drawer. Each sock has one of 1010 possible colours, which are represented by integers between 11 and 1010. Specifically, the colours of the socks are AA, BB, and CC.

# Chef has to wear two socks which have the same colour. Help Chef find out if that is possible or not.

# Input Format
# The first and only line of the input contains three space-separated integers AA, BB and CC.

# Output Format
# Print a single line containing the string "YES" if it is possible for Chef to wear two socks with the same colour or "NO"

# cook your dish here

(a, b, c) = map(int, input().split(' '))
if a ==b:
    print("YES")
elif a==c:
    print("YES")
elif b ==c:
    print("YES")
else:
    print("NO")