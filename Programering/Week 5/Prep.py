# def hello_world():
#     print("Hello, world!")
#     print("This is my first Python function!")

# hello_world()
# hello_world()


# def fancier_greet(name, day):
#     print("Greetings, my good fellow " + name + "!")
#     print("How are you doing this fine " + day + "?")

# fancier_greet("Anders", "Thursday")
# fancier_greet("Sandra", "Monday")


# def sum_and_print(x, y):
#     print(x + y)

# a = 5
# b = 10
# sum_and_print(2 * b, b + a)



# def another_greeting(name, day):
#     greeting = "Hello, " + name + "! What a lovely " + day + "!"
#     print(greeting)

# name = "Martin"
# day = "Wednesday"
# another_greeting(day, name)




# def silly_square(x):
#     k = -x * x
#     return k

# a = 5
# b = silly_square(a)
# print(b)

# print(type(b))
# print(type(silly_square(a)))


# def my_function(x, y):
#     k = x + y
#     if k > 10:
#         return k
#     return 0

# print(my_function(3, 4))
# print(my_function(30, 40))



# def another_function(hours):
#     if hours < 12:
#         return "Good morning!"
#     elif hours < 18:
#         return "Good afternoon!"
#     else:
#         return "Good evening!"

# print(another_function(15))




# def returning_expression(x):
#     return x * 2 + 20

# a = 10
# b = returning_expression(a)
# print(b)


# def is_even(x):
#     return x % 2 == 0
    
# print("Is 5 even?", is_even(5))
# print("Is 6 even?", is_even(6))



# def doing_two_things(name):
#     print("Hello, " + name + "!")
#     return "Your name is " + str(len(name)) + " characters long."
    
# comment = doing_two_things("Michael")
# print(comment)



# def say_hello():
#     print("Hello!")

# a = say_hello()
# print(a)



# def function_1(name, age):
#     print("Hi, " + name + ". When do you turn " + str(age + 1) + "?")

# function_1("Alice", 25)

# def function_2(name, age):
#     return "Hi, " + name + ". When do you turn " + str(age + 1) + "?"

# print(function_2("Alice", 25))




# def convert_imperial_to_metric(feet, inches):
#     length_in_inches = feet * 12 + inches
#     length_in_cm = length_in_inches * 2.54
#     return length_in_cm

# feet = 6
# inches = 2
# converted = convert_imperial_to_metric(feet, inches)
# print(converted)




# inch_per_cm = 2.54

# def convert_imperial_to_metric(feet, inches):
#     length_in_inches = feet * 12 + inches
#     length_in_cm = length_in_inches * inch_per_cm
#     return length_in_cm

# feet = 6
# inches = 2
# my_height_in_cm = convert_imperial_to_metric(feet, inches)
# print(my_height_in_cm)




# def add_one_to_x(x):
#     x = x + 4
#     print(x)
    
# x = 1
# add_one_to_x(x)
# print(x)



# def add_one_to_x(x):
#     x = x + 1
#     return x
    
# x = 1
# x = add_one_to_x(x)
# print(x)




# import math

# def disc_area(radius):
#     print("print 1")
#     return math.pi * radius ** 2

# def ring_area(inner_radius, outer_radius):
#     print("print 2")
#     return disc_area(outer_radius) - disc_area(inner_radius)

# print("print 3")
# inner_radius = 5
# outer_radius = 10
# area = ring_area(inner_radius, outer_radius)
# print(area)



# import math

# def ring_area(inner_radius, outer_radius):
#     return disc_area(outer_radius) - disc_area(inner_radius)

# def disc_area(radius):
#     return math.pi * radius ** 2

# print(ring_area(5, 10))



# def function_with_error():
#     a = 5
#     b = "The number is " 
#     print(b + a)

# function_with_error()




# def print_message(x):
#     print("For",  x, "the value is", compute(x))

# def inverse(x):
#     return 1 / x

# def compute(x):
#     return 2 * inverse(x)

# print_message(1)


# import math

# def square(x):
#     return x ** 2

# print("Testing the square function. These should all be True.")
# print("Test 1:", square(-3) == 9)
# print("Test 2:", square(0) == 0)
# print("Test 3:", square(1) == 1)
# print("Test 4:", square(2) == 4)
# print("Test 5:", square(25) == 625)




# def square(x):
#     return x ** 2

# def test_square():
#     test1 = square(-3) == 9
#     test2 = square(0) == 0
#     test3 = square(1) == 1
#     test4 = square(2) == 4
#     test5 = square(25) == 625

#     all_tests_passed = test1 and test2 and test3 and test4 and test5
#     return all_tests_passed

# if test_square():
#     print("Your function passed all tests.")
# else:
#     print("Your function did not pass all tests.")



# def calculate_density(mass, volume):
#     return mass / volume

# print(calculate_density(10, 2)) 



# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9

# print(convert_to_celsius(67))


# def calculate_velocity(distance, time):
#     return distance / time

# print(calculate_velocity(32, 10))
# print(calculate_velocity(32, 17))


# def factorial(n):
#     output = 1
#     for i in range(1, n + 1):
#         output = output * i
#     return output

# print("2 * 5! =", 2 * factorial(5))



# import math

# def cone_volume(radius, height):
#     return math.pi * (radius ** 2) * height / 3

# cone_volume34 = cone_volume(3, 4)
# print("The volume of a cone with radius 3 and height 4 is", cone_volume)
# cone_volume56 = cone_volume(5, 6)
# print("The volume of a cone with radius 5 and height 6 is", cone_volume)



# def get_greeting():
#     return "Hello there... "

# print(get_greeting() + "Simon")




# def print_message(message):
#     print("The message is:", message)

# print_message("Don't do this!")



# def print_message():
#     print("will A be first?")
#     return "will B be first?"

# print_message()


# def sum_numbers(n):
#     my_sum = 0
#     for i in range(1, n + 1):
#         my_sum = my_sum + i
#         return my_sum

# a = sum_numbers(3)

# print(a)



k = 3
def func(var):
    k = 13
    return k + var
print(k)
func(-1)
print(k)