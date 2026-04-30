age = 23
height = 1.82
complex_number = 3 + 4j

# area of this triangle (area = 0.5 x b x h).
base = input("Enter base : ")
height = input("Enter height : ")
area = 0.5 * int(base) * int(height)
print("The area of the traingle is " ,area)

#  Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input("Enter side a:")
side_b = input("Enter side b:")
side_c = input("Enter side c:")
triangle = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is " , triangle)

# rectangle 
lenght = input("Enter Length :")
width = input("Enter width : ")
area = int(lenght) * int(width)
perimeter = 2 * (int(lenght) + int(width))
print("The area of the rectangle is " , area)
print("The perimeter of the rectange is " ,perimeter)

#radius of a circle
radius = input("Enter radius :")
area = 3.14 * radius**2
circumference = 2 * 3.14 * radius
print("Area of a circle " , area)
print("Circulference of circle is " , circumference)

# y = 2x - 2

# Slope (coefficient of x)
slope_1 = 2

# Y-intercept (when x = 0)
y_intercept = -2

# X-intercept (when y = 0)
# 0 = 2x - 2
# 2x = 2
# x = 1
x_intercept = 1

print("Slope:", slope_1)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# Slope is (m = y2-y1/x2-x1) 

import math

# Points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope: m = (y2 - y1) / (x2 - x1)
slope = (y2 - y1) / (x2 - x1)
print("Slope:", slope)

# Euclidean distance: d = sqrt((x2-x1)² + (y2-y1)²)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean Distance:", distance)

#Compare the slopes in tasks 8 and 9. 
if slope > slope_1 :
    print("Slop one the greather than solope form task 8")
else :
    print("Slop one the greather than solope form task 9")

# where x is going to be 0 
for x in range(-100,100):
    y = x**2 + 6*x + 9
    if y == 0 :
        print("the value of x is :" , x )

# Length of both words
len_python = len('python')  # 6
len_dragon = len('dragon')  # 6

print("Length of python:", len_python)
print("Length of dragon:", len_dragon)

# Falsy comparison (they are equal so != gives False)
print(len_python != len_dragon)  # False

if 'on' in 'python' and 'on' in 'dragon':
    print("Found in both")
else:
    print("Not found in both")

statement = 'I hope this course is not full of jargon'
if "jargon" in statement:
    print("yes")
else :
    print("NO")

str_ = "python"
n = len(str_)
print(float(n))
print(str(n))

number = 8

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

print(7 // 3)        # 2
print(int(2.7))      # 2

print(7 // 3 == int(2.7))  # True

ty1 = type('10')
ty2 = type(10)
if not ty1 == ty2 :
    print("there are not equal")


int1 = (int('9.8'))
int2_ = (int(10))
if not int1 == int2_ :
    print("there are not equal")


hour = input("Enter hours :")
rate = input("Enter rate per hour :")
result = int(hour) * int(rate)
print("Your weekly earning is " , result)


year = input("Enter number of years you have lived: ")
# calculations
days = year * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"You have lived for {seconds} seconds.")

for i in range(1, 6):
    print(i, 1, i**1, i**2, i**3)