# You are given the height HH (in metres) and mass MM (in kilograms) of Chef. 
# The Body Mass Index (BMI) of a person is computed as \frac{M}{H^2} 

# Report the category into which Chef falls, based on his BMI:

# Category 1: Underweight if BMI \leq ≤18
# Category 2: Normal weight if BMI is ∈{19, 20,\…, 24}
# Category 3: Overweight if BMI \in \∈{25, 26,\…, 29}
# Category 4: Obesity if BMI \geq ≥30
# Input:
# The first line of input will contain an integer, TT, which denotes the number of testcases. Then the testcases follow.
# Each testcase contains a single line of input, with two space separated integers, M, HM,H, which denote the mass and height of Chef respectively.
# Output:
# For each testcase, output in a single line, 1, 2, 31,2,3 or 44, based on the category in which Chef falls.

# cook your dish here
t = int(input())

for i in range(t):
    (m,h) = map(int, input().split(' '))
    bmi = m/(h**2)
    if bmi <=18:
        print("1")#category1(Underweight)
    elif bmi >=19 and bmi<=24:
        print("2")#category 2(Normal weight)
    elif bmi >=25 and bmi<=29:
        print("3")#category 3(Overweight)
    else:
        print("4")#Obese