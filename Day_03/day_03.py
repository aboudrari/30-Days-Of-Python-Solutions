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