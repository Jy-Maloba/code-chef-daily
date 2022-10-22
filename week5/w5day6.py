# You are given an integer N. Find the largest integer between 1 and 10 (inclusive) which divides N.

n = int(input())
m = []
for i in range(1,11):
    if n%i==0:
        m.append(i)
m.sort()
print(m[-1])
        