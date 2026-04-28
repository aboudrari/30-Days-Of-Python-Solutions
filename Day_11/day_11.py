import math
def add_two_numbers (num1,num2):
    return (num1 + num2)

def area_of_circle (r):
    pi = math.pi
    return (pi * r**2)


def add_all_nums(*numbers):
    total = 0
    for num in numbers :
        if not int(num):
            print("Should be a number")
        else :
            total += num 
    return total

def convert_celsius_to_fahrenheit(c):
    # °F = (°C x 9/5) + 32
    f = (c * 9/5 ) + 32
    return f

def check_season(month):
    spring = ["March","April","May"]
    Summer = ["June","July ",'August']
    Autumn = ['September','October','November']
    Winter = ['December','January','February']
    if month in spring :
        print("Spring")
    elif month in Summer :
        print("Summer")
    elif month in Autumn :
        print ("Autumn")
    elif month in Winter :
        print("Winter")    

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)

    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)

    else:
        return ()
    
def print_list(lst):
    for item in lst :
        print(item)

def reverse_list(arr):
    return arr[::-1]

# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]

def capitalize_list_items(list_):
    new_lst = []
    for item in list_ :
        new_lst.append(item.capitalized())
    return new_lst

def add_item(lst , item) :
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

def remove_item(lst , item):
    lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(number):
    total = 0
    for num in range(1 , number +1):
        total += num
    return total

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050    
