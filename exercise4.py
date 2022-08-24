# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

#1 
print('Enter the lengths of three sides of a triangle:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

#2 & 3

# equilateral - all 3 sides are equal in length
if a == b == c:
    print(f'A triangle with sides of {a}, {b}, & {c} is a equilateral triangle.')

# scalene - all three sides are unequal in length
elif a !=b != c:
    print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')

# isosceles - two sides are the same length - do not need to create a statement here because we have already created a statement for other 2 triangles

else:
    print(f'A triangle with sides of {a}, {b} & {c} is a isosceles triangle')
