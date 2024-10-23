import math
from sympy import symbols, diff

## Opgave 1

# def f(x):
#     return 16*(x**3)-119*(x**2)+206*x-174

##Har det en rod?
# print(f(5))
# print(f(6))

#Definer værdier
# a=5
# b=6
# c=(a+b)/2
# print(f(c))
# d=(a+c)/2
# print(f(d))
# e=(d+c)/2
# print(f(e))
# g=(e+c)/2
# print(f(g))

# print(e)

## Opgave 3

# def f(x):
#     return 4*x**3+(25/8)*x**2-(57/4)*x+(89/4)


# a=-3
# b=-2
# #test af rod
# print(f(a))
# print(f(b))

# # while f(a)!=0:
# #     if f(a)<=0:
# #         a1=(a+b)/2
# #         if a1<0:
# #             a=a1
# #     else:
# #         b1=(a+b)/2
# #         if b1>0:
# #             b=b1
# #     print(str(f(a))+" = funktion")
# # print(str(a)+str(b)+" svar")


# b1=(a+b)/2
# print(f(b1))
# b2=(a+b1)/2
# print(f(b2))
# a1=(a+b2)/2
# print(f(a1))
# a2=(a1+b2)/2
# print(f(a2))
# a3=(a2+b2)/2
# print(f(a3))
# b3=(a3+b2)/2
# print(f(b2))
# b4=(a3+b3)/2
# print(f(b4))
# b5=(a3+b4)/2
# print(f(b5))
# b6=(a3+b5)/2
# print(f(b6))
# b7=(a3+b6)/2
# print(f(b7))
# b8=(a3+b7)/2
# print(f(b8))
# b9=(a3+b8)/2
# print(f(b9))
# b10=(a3+b9)/2
# print(f(b10))
# b11=(a3+b10)/2
# print(f(b11))
# b12=(a3+b11)/2
# print(f(b12))
# b13=(a3+b12)/2
# print(f(b13))
# b14=(a3+b13)/2
# print(f(b14))
# b15=(a3+b14)/2
# print(f(b15))
# b16=(a3+b15)/2
# print(f(b16))
# b17=(a3+b16)/2
# print(f(b17))
# print(b17)

# print(b1)
# print(b2)
# print(a1)
# print(a2)
# print(a3)

## Opgave 4

# def f(x):
#     return 4*x**3+(25/4)*x**2-(41/2)*x+(57/2)

# def fm(x):
#     return 12*x**2+12.5*x-20.5

# # x0=-3
# # x1=x0-(f(x0)/fm(x0))
# # print(x1)

# x=-3
# for i in range(3):
#     x=x-(f(x)/fm(x))
#     print(x)
# print("x0 = "+str(x))

# y=-3
# for i in range(16):
#     y=y-f(y)/fm(y)
#     print(y)
# print("x1 = "+str(y))


## Opgave 5

import math

# Define the function f(x)
def f(x):
    return math.sin(x) - 0.5 * x

# Define the derivative f'(x)
def f_prime(x):
    return math.cos(x) - 0.5

# Newton-Raphson method
def newton_raphson(x0, tolerance=1e-7, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fx) < tolerance:
            return x  # root found
        if fpx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x = x - fx / fpx
    raise ValueError("Maximum iterations reached. No solution found.")

# Initial guess (let's use a value between 0 and pi)
x0 = math.pi / 2

# Call the Newton-Raphson method
solution = newton_raphson(x0)

print(solution)




