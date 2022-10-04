# Problem
# The fuel economy of a car is the distance which it can travel on one litre of fuel.

# The base fuel economy (i.e, its fuel economy when there is only one person - the driver - in the car) of a certain car is MM kilometres per litre. It was also observed that every extra passenger in the car decreases the fuel economy by 11 kilometre per litre.

# PP people want to take this car for a journey. They know that the car currently has VV litres of fuel in its tank.

# What is the maximum distance this car can travel under the given conditions, assuming that all PP people always stay in the car and no refuelling can be done?

# Note that among the PP people is also a driver, i.e, there are exactly PP people in the car.

# Input Format
# The first line of input contains a single integer TT, denoting the number of test cases. The description of TT test cases follows.
# Each test case consists of a single line of input, containing three space-separated integers P, MP,M, and VV - the number of people, base fuel economy, and amount of fuel present in the car, respectively.
# Output Format
# For each test case, output a single line containing one integer - the maximum distance that the car can travel.

# cook your dish here
t = int(input())

for i in range(t):
    (p, m, v) = map(int, input().split(' '))
    if(p>1):
        print((m-p+1)*v)
    else:
        print(m*v)